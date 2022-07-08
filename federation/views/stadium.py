from logging import getLogger
from rest_framework.generics import CreateAPIView

from core.permissions import IsFederationAgentOrReadOnly

from ..models import Stadium, StadiumSeatPlace
from ..serializers import StadiumSerializer
from ..tasks import create_stadium_seat_place

logger = getLogger(__name__)


class CreateStadiumAPIView(CreateAPIView):
    serializer_class = StadiumSerializer
    permission_classes = (IsFederationAgentOrReadOnly, )

    def perform_create(self, serializer):
        instance: Stadium = serializer.save()
        create_stadium_seat_place.delay(instance.id)
        return instance
