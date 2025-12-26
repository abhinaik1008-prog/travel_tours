from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Destination
from .serializers import DestinationSerializer


class DestinationListAPIView(ListAPIView):
    queryset = Destination.objects.filter(is_active=True)
    serializer_class = DestinationSerializer
    permission_classes = [AllowAny]   # 👈 THIS LINE FIXES IT
