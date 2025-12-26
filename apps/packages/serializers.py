from rest_framework import serializers
from .models import (
    Package, 
    PackageImage, 
    Availability, 
    PopularPackage
)

class PackageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageImage
        fields = ('image_url',)


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ('start_date', 'end_date', 'slots')


class PackageSerializer(serializers.ModelSerializer):
    images = PackageImageSerializer(many=True, read_only=True)
    availability = AvailabilitySerializer(many=True, read_only=True)
    destination = serializers.StringRelatedField()

    class Meta:
        model = Package
        fields = (
            'id',
            'title',
            'destination',
            'price',
            'duration_days',
            'description',
            'inclusions',
            'exclusions',
            'images',
            'availability',
        )


class PopularPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularPackage
        fields = "__all__"