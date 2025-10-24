from django.shortcuts import render
from django.http import JsonResponse
from .models import Property
from rest_framework import viewsets, permissions
from .models import Property
from .serializers import PropertySerializer
from .permissions import IsHostOrReadOnly


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


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsHostOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)