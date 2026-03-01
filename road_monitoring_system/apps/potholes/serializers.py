from rest_framework import serializers
from .models import PotholeEvent


class PotholeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotholeEvent
        fields = [
            'id',
            'latitude',
            'longitude',
            'vibration_value',
            'severity',
            'image',
            'created_at',
        ]
        read_only_fields = ['id', 'severity', 'created_at']