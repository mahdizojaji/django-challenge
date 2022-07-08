from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager

from . import BaseModel
from ..managers import CustomBaseManager


class CustomUserManager(BaseUserManager, CustomBaseManager):
    def create_user(self, phone_number, password, is_staff=False, is_superuser=False, is_active=True, **extra_fields):
        if not phone_number:
            raise ValueError("Users must have a phone_number")
        if not password:
            raise ValueError("Users must have a password")

        user_obj = self.model(
            phone_number=phone_number,
            **extra_fields,
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, phone_number, password=None, **extra_fields):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields,
        )
        return user


class CustomUser(BaseModel, AbstractUser):
    objects = CustomUserManager()
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=32,
        null=True, blank=True,
        unique=True,
    )
    phone_number = models.CharField(
        verbose_name=_('Phone Number'),
        max_length=32,
        unique=True,
    )
    last_otp_sent = models.DateTimeField(
        verbose_name=_('Last time of otp sent'),
        null=True, blank=True,
    )
    is_federation_agent = models.BooleanField(
        verbose_name=_('Is federation agent?'),
        default=False,
    )
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
