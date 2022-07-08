from logging import getLogger

from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from ..models import Match, MatchSeatPlace, StadiumSeatPlace
from ..serializers import MatchSeatPlaceSerializer

logger = getLogger(__name__)


class BuyMatchSeatPlaceAPIView(CreateAPIView):
    serializer_class = MatchSeatPlaceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Match.objects.all()

    def perform_create(self, serializer):
        match = self.get_object()
        stadium_seat_place: StadiumSeatPlace = serializer.validated_data['stadium_seat_place']
        if stadium_seat_place.status != StadiumSeatPlace.STATUS_HEALTHY:
            raise ValidationError({'stadium_seat_place': 'SeatPlace is not ready.'})
        if MatchSeatPlace.objects.filter(match=match, stadium_seat_place=stadium_seat_place):
            raise ValidationError({'stadium_seat_place': 'SeatPlace already reserved.'})
        serializer.save(user=self.request.user, status=MatchSeatPlace.STATUS_PAID, match=match)
