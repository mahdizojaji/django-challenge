import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


from ..managers import CustomBaseManager


class BaseModel(models.Model):
    """BaseModel class"""

    objects = CustomBaseManager()
    uuid = models.UUIDField(
        verbose_name=_('UUID'),
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated at'),
        auto_now=True,
    )

    class Meta:
        abstract = True
