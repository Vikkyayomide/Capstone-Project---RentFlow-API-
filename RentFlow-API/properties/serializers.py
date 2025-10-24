from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'host', 'title', 'description', 'price_per_night', 'location', 'max_guests', 'bedrooms', 'bathrooms', 'amenities', 'created_at', 'updated_at']