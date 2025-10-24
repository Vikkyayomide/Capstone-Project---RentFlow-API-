# Capstone-Project---RentFlow-API-
A Django REST Framework backend for property rentals. Hosts can list properties and guests can book available stays.

# RentFlow API - Property Rental Backend

A complete Django REST API for property rental management system.

## 🚀 Features

- **Property Management**: List, view, search properties
- **Booking System**: Make reservations with date validation  
- **RESTful API**: Clean JSON endpoints
- **Admin Interface**: Django admin for data management
- **Database Relationships**: Proper ForeignKey and ManyToMany relationships

## 🛠️ Tech Stack

- **Backend**: Django & Django REST Framework
- **Database**: SQLite (development)
- **Authentication**: JWT (ready for implementation)
- **API Documentation**: Built-in DRF browsable API

## 📋 API Endpoints

### Properties
- `GET /api/properties/` - List all properties
- `GET /api/properties/{id}/` - Get property details  
- `GET /api/properties/search/` - Search with filters (location, price, dates)
- `POST /api/properties/` - Create new property

### Bookings
- `GET /api/bookings/` - List all bookings
- `POST /api/bookings/` - Create new booking with date validation

### Authentication (Ready for extension)
- `POST /api/token/` - JWT token obtain
- `POST /api/token/refresh/` - JWT token refresh

## 🏗️ Project Structure

