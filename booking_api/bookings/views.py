# bookings/views.py
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Booking
from .serializers import BookingSerializer

from rest_framework.permissions import IsAuthenticated

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['date']  # You can add more fields here
    search_fields = ['name', 'email']
    ordering_fields = ['date', 'created_at']
    permission_classes = [IsAuthenticated]
