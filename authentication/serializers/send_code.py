from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

from rest_framework.serializers import ModelSerializer

User = get_user_model()


class SendCodeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number",)
        extra_kwargs = {
            "phone_number": {
                "validators": [
                    RegexValidator(regex=settings.PHONE_NUMBER_PATTERN, message="Phone number pattern is wrong."),
                ],
            }
        }
