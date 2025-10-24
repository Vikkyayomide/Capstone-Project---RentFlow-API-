from django.shortcuts import render
from django.http import JsonResponse
from .models import Property

def property_list(request):
    properties = Property.objects.all()
    property_data = []
    for property in properties:
        property_data.append({
            'id': property.id,
            'title': property.title,
            'price': str(property.price_per_night),
            'location': property.location
        })
    return JsonResponse({'properties': property_data})