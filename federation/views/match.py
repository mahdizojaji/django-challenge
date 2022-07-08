from logging import getLogger
from rest_framework.generics import CreateAPIView

from core.permissions import IsFederationAgentOrReadOnly

from ..serializers import MatchSerializer

logger = getLogger(__name__)


class CreateMatchAPIView(CreateAPIView):
    serializer_class = MatchSerializer
    permission_classes = (IsFederationAgentOrReadOnly, )
