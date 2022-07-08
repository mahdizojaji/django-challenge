from logging import getLogger
from rest_framework.generics import CreateAPIView

from core.permissions import IsFederationAgentOrReadOnly

from ..serializers import StadiumSerializer

logger = getLogger(__name__)


class CreateStadiumAPIView(CreateAPIView):
    serializer_class = StadiumSerializer
    permission_classes = (IsFederationAgentOrReadOnly, )
