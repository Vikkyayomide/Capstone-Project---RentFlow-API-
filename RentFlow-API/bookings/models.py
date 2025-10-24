from django.db import models

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    guest = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='bookings')
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)  # When booking was made

    def __str__(self):
        return f"{self.guest.username} - {self.property.title}"