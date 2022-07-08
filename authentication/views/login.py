from logging import getLogger

from datetime import datetime, timedelta

from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model, authenticate

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, serializers

from dj_rest_auth.views import LoginView
from dj_rest_auth.utils import jwt_encode

from core.models import CustomUser

from ..serializers import LoginSerializer


User: CustomUser = get_user_model()

logger = getLogger(__name__)


class LoginAPIView(LoginView):
    refresh_token: str
    request: Request
    serializer: serializers.Serializer
    serializer_class = LoginSerializer

    def login(self):
        self.access_token, self.refresh_token = jwt_encode(self.user)
        self.process_login()

    def post(self, request: Request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        phone = self.serializer.validated_data["phone_number"]
        code = self.serializer.validated_data["password"]
        # authenticate user
        user: CustomUser = authenticate(
            phone_number=phone,
            password=code,
        )
        if user:
            # checking code expire time
            if all([
                user.last_otp_sent,
                user.last_otp_sent + timedelta(seconds=settings.SMS['OTP_EXPIRE']) > timezone.now()
            ]):
                self.user = user
                self.login()
                user.set_unusable_password()
                user.save(update_fields=['password'])
                # THE HAPPY ENDING ~>
                return self.get_response()
            else:
                response = {
                    "error": "auth-expire",
                    "message": "Authentication failed.",
                    "detail": "Login code expired.",
                }
        else:
            response = {
                "error": "auth-code",
                "message": "Authentication failed.",
                "detail": "Phone number or code is not valid.",
            }
        return Response(
            response,
            status=status.HTTP_401_UNAUTHORIZED,
        )
