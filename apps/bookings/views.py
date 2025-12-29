from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookingCreateAPIView(APIView):
    def post(self, request):
        # later you will save booking here
        return Response(
            {"status": "success", "message": "Booking created"},
            status=status.HTTP_201_CREATED
        )


class MyBookingsAPIView(APIView):
    def get(self, request):
        # later you will filter by user
        return Response(
            {"status": "success", "data": []},
            status=status.HTTP_200_OK
        )
