from rest_framework.serializers import ModelSerializer

from ..models import Stadium


class StadiumSerializer(ModelSerializer):
    class Meta:
        model = Stadium
        fields = ("id", "uuid", 'name', 'capacity')
        read_only_fields = ('id', 'uuid')
