from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Booking

class BookingAPITestCase(APITestCase):
    def setUp(self):
        self.booking_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'date': '2025-07-25',
            'time': '12:00'
        }
        self.list_create_url = reverse('booking-list')

        # Create a booking to use in retrieve, update, delete tests
        self.booking = Booking.objects.create(**self.booking_data)

    def test_create_booking(self):
        data = {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'date': '2025-07-26',
            'time': '14:00'
        }
        response = self.client.post(self.list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)

    def test_list_bookings(self):
        response = self.client.get(self.list_create_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_booking(self):
        url = reverse('booking-detail', args=[self.booking.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.booking.email)

    def test_update_booking(self):
        url = reverse('booking-detail', args=[self.booking.id])
        updated_data = self.booking_data.copy()
        updated_data['name'] = 'John Updated'

        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.name, 'John Updated')

    def test_delete_booking(self):
        url = reverse('booking-detail', args=[self.booking.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)


def test_prevent_duplicate_booking(self):
    duplicate_data = {
        'name': 'Another Person',
        'email': self.booking_data['email'],
        'date': self.booking_data['date'],
        'time': self.booking_data['time']  # Same time to match
    }
    response = self.client.post(self.list_create_url, duplicate_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
