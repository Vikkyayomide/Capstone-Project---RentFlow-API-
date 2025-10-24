from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Booking
from properties.models import Property
from django.contrib.auth.models import User

@csrf_exempt
def booking_list(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        booking_data = []
        for booking in bookings:
            booking_data.append({
                'id': booking.id,
                'property': booking.property.title,
                'guest': booking.guest.username if booking.guest else 'Anonymous',
                'check_in': booking.check_in_date.isoformat(),
                'check_out': booking.check_out_date.isoformat(),
                'total_price': str(booking.total_price),
                'status': booking.status
            })
        return JsonResponse({'bookings': booking_data})

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            property_id = data['property_id']
            check_in_str = data['check_in_date']
            check_out_str = data['check_out_date']
            guests = int(data.get('guests', 1))

            

            property = Property.objects.get(id=property_id)
            user = User.objects.first()  # For testing, use the first user

            # Calculate total price (for simplicity, assume 1 night)
            total_price = property.price_per_night

            booking = Booking.objects.create(
                guest=user,
                property=property,
                check_in_date=check_in_str,
                check_out_date=check_out_str,
                total_price=total_price,
                status='pending'
            )

            return JsonResponse({
                'id': booking.id,
                'property': property.title,
                'check_in': booking.check_in_date.isoformat(),
                'check_out': booking.check_out_date.isoformat(),
                'total_price': str(total_price),
                'status': booking.status,
                'message': 'Booking created successfully'
            }, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)