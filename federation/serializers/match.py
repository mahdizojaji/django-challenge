from rest_framework.serializers import ModelSerializer

from core.seriazlier_fields import TimestampField

from ..models import Match


class MatchSerializer(ModelSerializer):
    datetime = TimestampField()
    purchase_deadline = TimestampField()

    class Meta:
        model = Match
        fields = ("id", "uuid", 'host_team', 'guest_team', 'stadium', 'datetime', 'duration', 'purchase_deadline')
        read_only_fields = ('id', 'uuid')
