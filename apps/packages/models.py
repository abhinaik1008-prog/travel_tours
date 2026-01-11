from django.db import models


class PopularPackage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    region = models.CharField(max_length=100)

    days = models.PositiveIntegerField()
    nights = models.PositiveIntegerField()
    pax = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    reviews_count = models.PositiveIntegerField(default=0)

    TRANSPORT_CHOICES = [("flight", "Flight"), ("ac_bus", "AC Sleeper Bus"), ("pushback_bus", "Pushback Bus"), ("train", "Train")]
    transport_type = models.CharField(max_length=20, choices=TRANSPORT_CHOICES, blank=True)

    HOTEL_CHOICES = [("3_star", "3 Star"), ("deluxe", "Deluxe"), ("premium", "Premium")]
    hotel_category = models.CharField(max_length=20, choices=HOTEL_CHOICES, blank=True)

    ROOM_CHOICES = [("common", "Common Hall"), ("four_share", "4 Sharing"), ("double", "Double Sharing")]
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES, blank=True)

    meals_included = models.BooleanField(default=True)
    sightseeing_included = models.BooleanField(default=True)
    tour_guide = models.BooleanField(default=True)

    places_covered = models.TextField(null=True, blank=True)

    offer_title = models.CharField(max_length=200, blank=True)
    has_offer = models.BooleanField(default=False)

    image = models.ImageField(upload_to="popular_packages/", null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_bookable = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
