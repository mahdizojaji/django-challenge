from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class Team(BaseModel):
    name = models.CharField(
        verbose_name=_('Team name'),
        max_length=100,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')
