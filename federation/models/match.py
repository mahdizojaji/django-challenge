from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


class Match(BaseModel):
    host_team = models.ForeignKey(
        verbose_name=_('Host Team'),
        to='federation.Team',
        on_delete=models.CASCADE,
        related_name='host_matches',
    )
    guest_team = models.ForeignKey(
        verbose_name=_('Guest Team'),
        to='federation.Team',
        on_delete=models.CASCADE,
        related_name='guest_matches',
    )
    stadium = models.ForeignKey(
        verbose_name=_('Stadium'),
        to='federation.Stadium',
        on_delete=models.CASCADE,
        related_name='matches',
    )
    datetime = models.DateTimeField(verbose_name=_('Date/Time of Match'))
    duration = models.DurationField(verbose_name=_('Duration'))
    purchase_deadline = models.DateTimeField(verbose_name=_('Ticket purchase deadline'))

    def clean(self):
        if self.host_team == self.guest_team:
            raise ValidationError('Host team could\'nt equal guest team')

        if self.purchase_deadline > self.datetime:
            raise ValidationError('Purchase deadline could\'nt after datetime of match')

        # TODO: Need to check in this time match exists

    def __str__(self):
        return f'{self.host_team} - {self.guest_team} | {self.datetime}'

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')
