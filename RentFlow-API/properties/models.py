from django.db import models
from django.db import models

# Amenity
class Amenity(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Property (which uses Amenity)
class Property(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('villa', 'Villa'),
        ('condo', 'Condo'),
    ]
    
    host = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, default='apartment')
    location = models.CharField(max_length=200)
    max_guests = models.IntegerField()
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.ManyToManyField(Amenity, related_name='properties') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title