from django.urls import path
from .views import DestinationListAPIView

urlpatterns = [
    path('destinations/', DestinationListAPIView.as_view(), name='destination-list'),
]
