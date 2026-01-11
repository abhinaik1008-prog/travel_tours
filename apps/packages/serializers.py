from rest_framework import serializers
from .models import PopularPackage


class PopularPackageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = PopularPackage
        fields = [
            "id",
            "title",
            "description",
            "region",
            "days",
            "nights",
            "pax",
            "price",
            "rating",
            "reviews_count",
            "transport_type",
            "hotel_category",
            "room_type",
            "meals_included",
            "sightseeing_included",
            "tour_guide",
            "places_covered",
            "offer_title",
            "has_offer",
            "image",
            "is_active",
            "is_bookable",
        ]

    def get_image(self, obj):
        """
        Return absolute image URL if image exists
        """
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
