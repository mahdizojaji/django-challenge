from rest_framework import serializers

from datetime import datetime


class TimestampField(serializers.DateTimeField):
    """
    Convert a django datetime to/from timestamp.
    """
    def to_representation(self, value):
        """
        Convert the field to its internal representation (aka timestamp)
        :param value: the DateTime value
        :return: a UTC timestamp integer
        """
        converted = datetime.fromisoformat(value)
        return int(converted.timestamp())

    def to_internal_value(self, value):
        """
        deserialize a timestamp to a DateTime value
        :param value: the timestamp value
        :return: a django DateTime value
        """
        converted = datetime.fromtimestamp(int(value))
        return super(TimestampField, self).to_representation(converted)