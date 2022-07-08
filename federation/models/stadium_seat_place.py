from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class StadiumSeatPlace(BaseModel):
    STATUS_HEALTHY = 0
    STATUS_BROKEN = 1
    STATUS_REPAIR = 2
    _STATUS_CHOICES = (
        (STATUS_HEALTHY, _('Healthy')),
        (STATUS_BROKEN, _('Broken')),
        (STATUS_REPAIR, _('Repair')),
    )
    stadium_seat_id = models.IntegerField(verbose_name=_('Stadium seat ID'))
    stadium = models.ForeignKey(
        verbose_name=_('Stadium'),
        to='federation.Stadium',
        on_delete=models.CASCADE,
        related_name='seat_places',
    )
    status = models.IntegerField(
        verbose_name=_('Status'),
        choices=_STATUS_CHOICES,
        default=STATUS_HEALTHY,
    )

    def __str__(self):
        return f'seat id {self.stadium_seat_id} of {self.stadium}'

    class Meta:
        unique_together = ('stadium_seat_id', 'stadium')
        verbose_name = _('Stadium seat place')
        verbose_name_plural = _('Stadium seat places')
