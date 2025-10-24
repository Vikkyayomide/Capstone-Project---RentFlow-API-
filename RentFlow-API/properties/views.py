from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Property

@csrf_exempt
def property_list(request):
    """GET /api/properties/ - List all properties"""
    if request.method == 'GET':
        properties = Property.objects.all()
        property_data = []
        for property in properties:
            property_data.append({
                'id': property.id,
                'title': property.title,
                'price': str(property.price_per_night),
                'location': property.location,
                'max_guests': property.max_guests
            })
        return JsonResponse({'properties': property_data})
    
    # POST /api/properties/ - Create new property
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            property = Property.objects.create(
                title=data['title'],
                description=data.get('description', ''),
                price_per_night=data['price_per_night'],
                location=data['location'],
                max_guests=data['max_guests'],
                bedrooms=data.get('bedrooms', 1),
                bathrooms=data.get('bathrooms', 1)
            )
            return JsonResponse({
                'id': property.id,
                'title': property.title,
                'message': 'Property created successfully'
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def property_detail(request, property_id):
    """GET /api/properties/1/ - Get property details"""
    try:
        property = Property.objects.get(id=property_id)
        property_data = {
            'id': property.id,
            'title': property.title,
            'description': property.description,
            'price': str(property.price_per_night),
            'location': property.location,
            'max_guests': property.max_guests,
            'bedrooms': property.bedrooms,
            'bathrooms': property.bathrooms,
            'host': property.host.username if property.host else 'Unknown'
        }
        return JsonResponse(property_data)
    except Property.DoesNotExist:
        return JsonResponse({'error': 'Property not found'}, status=404)

def property_search(request):
    """GET /api/properties/search/ - Search properties with filters"""
    try:
        # Get all possible filters
        location = request.GET.get('location', '')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        guests = request.GET.get('guests')
        property_type = request.GET.get('property_type')
        min_bedrooms = request.GET.get('min_bedrooms')
        min_bathrooms = request.GET.get('min_bathrooms')
        
        # Start with all properties
        properties = Property.objects.all()
        
        # Apply filters
        if location:
            properties = properties.filter(location__icontains=location)
        if min_price:
            properties = properties.filter(price_per_night__gte=min_price)
        if max_price:
            properties = properties.filter(price_per_night__lte=max_price)
        if guests:
            properties = properties.filter(max_guests__gte=guests)
        if property_type:
            properties = properties.filter(property_type=property_type)
        if min_bedrooms:
            properties = properties.filter(bedrooms__gte=min_bedrooms)
        if min_bathrooms:
            properties = properties.filter(bathrooms__gte=min_bathrooms)
        
        # Prepare response data
        property_data = []
        for property in properties:
            # Get amenities for this property
            amenity_names = [amenity.name for amenity in property.amenities.all()]
            
            property_data.append({
                'id': property.id,
                'title': property.title,
                'description': property.description,
                'price': str(property.price_per_night),
                'location': property.location,
                'max_guests': property.max_guests,
                'bedrooms': property.bedrooms,
                'bathrooms': property.bathrooms,
                'property_type': property.property_type,
                'host': property.host.username if property.host else 'Unknown',
                'amenities': amenity_names,
                'created_at': property.created_at.isoformat()
            })
        
        return JsonResponse({
            'count': properties.count(),
            'filters_applied': {
                'location': location,
                'min_price': min_price,
                'max_price': max_price,
                'guests': guests,
                'property_type': property_type,
                'min_bedrooms': min_bedrooms,
                'min_bathrooms': min_bathrooms
            },
            'properties': property_data
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)