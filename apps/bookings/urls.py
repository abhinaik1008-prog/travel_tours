from django.urls import path
from .views import BookingCreateAPIView, MyBookingsAPIView

urlpatterns = [
    path('bookings/', BookingCreateAPIView.as_view()),
    path('bookings/my/', MyBookingsAPIView.as_view()),
]
