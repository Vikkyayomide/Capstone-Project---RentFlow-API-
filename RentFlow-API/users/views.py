from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserProfile
import json

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """Get current user's profile"""
    user = request.user
    profile = user.profile
    
    return Response({
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_joined': user.date_joined
        },
        'profile': {
            'phone_number': profile.phone_number,
            'bio': profile.bio,
            'is_host': profile.is_host,
            'profile_picture': profile.profile_picture.url if profile.profile_picture else None
        }
    })

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    """Update user profile"""
    try:
        user = request.user
        profile = user.profile
        data = request.data
        
        # Update user fields
        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        if 'email' in data:
            user.email = data['email']
        user.save()
        
        # Update profile fields
        if 'phone_number' in data:
            profile.phone_number = data['phone_number']
        if 'bio' in data:
            profile.bio = data['bio']
        if 'is_host' in data:
            profile.is_host = data['is_host']
        profile.save()
        
        return Response({'message': 'Profile updated successfully'})
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_properties(request):
    """Get properties owned by current user"""
    from properties.models import Property
    
    properties = Property.objects.filter(host=request.user)
    property_data = []
    for property in properties:
        property_data.append({
            'id': property.id,
            'title': property.title,
            'price': str(property.price_per_night),
            'location': property.location,
            'status': 'active',
            'created_at': property.created_at.isoformat()
        })
    
    return Response({
        'count': properties.count(),
        'properties': property_data
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_bookings(request):
    """Get bookings made by current user"""
    from bookings.models import Booking
    
    bookings = Booking.objects.filter(guest=request.user)
    booking_data = []
    for booking in bookings:
        booking_data.append({
            'id': booking.id,
            'property_title': booking.property.title,
            'property_location': booking.property.location,
            'check_in': booking.check_in_date.isoformat(),
            'check_out': booking.check_out_date.isoformat(),
            'total_price': str(booking.total_price),
            'status': booking.status,
            'created_at': booking.created_at.isoformat()
        })
    
    return Response({
        'count': bookings.count(),
        'bookings': booking_data
    })
