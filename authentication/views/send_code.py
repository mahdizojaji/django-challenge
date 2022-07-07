from logging import getLogger, INFO

from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView

from core.models import CustomUser
from extensions.sms import generate_random_code, send_otp_sms

from ..serializers import SendCodeSerializer

User: CustomUser = get_user_model()

logger = getLogger(__name__)


class SendCodeAPIView(GenericAPIView):
    serializer_class = SendCodeSerializer

    def post(self, request, *args, **kwargs):
        # validating serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # get or create user
        user, _ = User.objects.get_or_create(
            phone_number=serializer.validated_data["phone_number"]
        )
        if user.is_staff:
            return Response(
                {
                    "error": "auth-sms",
                    "message": "Failed to send SMS.",
                    "detail": "You are not allowed to login with this phone number",
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        otp_code = f"{generate_random_code()}"

        # Notify otp code
        if settings.SMS["DEBUG_MODE"]:
            logger.debug(f'OTP code of {user.phone_number} is: {otp_code}')
            sms_success, sms_error = True, None
        else:
            # generating random code
            sms_response = send_otp_sms(user.phone_number, otp_code).json()
            sms_success = (
                True if sms_response.get("result", {}).get("code") == 200 else False
            )
            sms_error = (
                None if sms_success else sms_response.get("result", {}).get("message")
            )

        # set otp as user password
        user.set_password(otp_code)
        # set code expire time
        user.last_otp_sent = timezone.now()
        user.save(update_fields=['last_otp_sent', 'password'])
        # response based on sms success
        if sms_success:
            # success response
            return Response(
                {
                    "ok": True,
                    "phone_number": user.phone_number,
                    "expire": int(user.last_otp_sent.timestamp() + settings.SMS['OTP_EXPIRE']),
                },
                status=status.HTTP_200_OK,
            )
        else:
            # fail response
            return Response(
                {
                    "error": "auth-sms",
                    "message": "Failed to send SMS.",
                    "detail": sms_error,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
