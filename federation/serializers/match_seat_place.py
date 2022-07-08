from rest_framework.serializers import ModelSerializer

from ..models import MatchSeatPlace


class MatchSeatPlaceSerializer(ModelSerializer):
    class Meta:
        model = MatchSeatPlace
        fields = ("uuid", 'match', 'stadium_seat_place')
        read_only_fields = ('uuid', 'match')
