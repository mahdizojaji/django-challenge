from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class Stadium(BaseModel):
    name = models.CharField(
        verbose_name=_('Stadium name'),
        max_length=100,
    )
    capacity = models.IntegerField(
        verbose_name=_('Capacity'),
    )

    def __str__(self):
        return f'{self.name}'
