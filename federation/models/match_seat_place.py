from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


User = get_user_model()


class MatchSeatPlace(BaseModel):
    STATUS_RESERVED = 0
    STATUS_PAID = 1
    _STATUS_CHOICES = (
        (STATUS_RESERVED, _('Reserved')),
        (STATUS_PAID, _('Paid')),
    )
    match = models.ForeignKey(
        verbose_name=_('Match'),
        to='federation.Match',
        on_delete=models.CASCADE,
        related_name='seat_places',
    )
    stadium_seat_place = models.ForeignKey(
        verbose_name=_('Seat Place'),
        to='federation.StadiumSeatPlace',
        on_delete=models.CASCADE,
        related_name='match_seat_places',
    )
    user = models.ForeignKey(
        verbose_name=_('User'),
        to=User,
        on_delete=models.CASCADE,
        related_name='seat_places',
    )
    status = models.IntegerField(
        verbose_name=_('Status'),
        choices=_STATUS_CHOICES,
        default=STATUS_RESERVED,
    )

    def __str__(self):
        return f'{self.stadium_seat_place} of match {self.match}'

    class Meta:
        verbose_name = _('Match seat place')
        verbose_name_plural = _('Match seat places')
