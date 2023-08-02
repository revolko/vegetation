from rest_framework import serializers

from .models import Plant


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'name', 'description', 'last_watered', 'water_frequency_summer', 'water_frequency_winter',
                  'watering_type', 'drought_tolerance', 'light_requirement')
