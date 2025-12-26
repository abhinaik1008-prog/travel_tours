from rest_framework import serializers
from .models import Booking
from apps.packages.models import Package

class BookingCreateSerializer(serializers.ModelSerializer):
    package_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Booking
        fields = (
            'package_id',
            'travel_date',
            'number_of_people',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        package_id = validated_data.pop('package_id')
        package = Package.objects.get(id=package_id)

        total_price = package.price * validated_data['number_of_people']

        booking = Booking.objects.create(
            user=user,
            package=package,
            total_price=total_price,
            status='PENDING',
            **validated_data
        )
        return booking


class BookingListSerializer(serializers.ModelSerializer):
    package = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = (
            'id',
            'package',
            'travel_date',
            'number_of_people',
            'total_price',
            'status',
            'created_at',
        )