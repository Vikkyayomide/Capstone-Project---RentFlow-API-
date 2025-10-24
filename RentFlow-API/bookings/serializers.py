from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'guest', 'property', 'check_in_date', 'check_out_date', 'total_price', 'status', 'created_at']