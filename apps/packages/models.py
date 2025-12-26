from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.country}"


class Package(models.Model):
    title = models.CharField(max_length=150)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField()
    description = models.TextField()
    inclusions = models.TextField()
    exclusions = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PackageImage(models.Model):
    package = models.ForeignKey(
        Package,
        related_name='images',
        on_delete=models.CASCADE
    )
    image_url = models.ImageField(upload_to='packages/')

    def __str__(self):
        return f"Image for {self.package.title}"


class Availability(models.Model):
    package = models.ForeignKey(
        Package,
        related_name='availability',
        on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.package.title} ({self.start_date} → {self.end_date})"



class PopularPackage(models.Model):

    # ================= BASIC INFO =================
    title = models.CharField(max_length=200)
    description = models.TextField()

    region = models.CharField(
        max_length=100,
        help_text="South India, North India, International etc."
    )

    # ================= DURATION =================
    days = models.PositiveIntegerField()
    nights = models.PositiveIntegerField()

    departure_date = models.DateField(
        null=True,
        blank=True,
        help_text="Fixed departure date (optional)"
    )

    # ================= GROUP DETAILS =================
    pax = models.PositiveIntegerField(
        help_text="Number of people in a group"
    )

    # ================= PRICING =================
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price per person"
    )

    # ================= RATINGS =================
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=5.0
    )
    reviews_count = models.PositiveIntegerField(default=0)

    # ================= TRANSPORT & STAY =================
    TRANSPORT_CHOICES = [
        ("flight", "Flight"),
        ("ac_bus", "AC Sleeper Bus"),
        ("pushback_bus", "Pushback Bus"),
        ("train", "Train"),
    ]
    transport_type = models.CharField(
        max_length=20,
        choices=TRANSPORT_CHOICES,
        blank=True
    )

    HOTEL_CHOICES = [
        ("3_star", "3 Star"),
        ("deluxe", "Deluxe"),
        ("premium", "Premium"),
    ]
    hotel_category = models.CharField(
        max_length=20,
        choices=HOTEL_CHOICES,
        blank=True
    )

    ROOM_CHOICES = [
        ("common", "Common Hall"),
        ("four_share", "4 Sharing"),
        ("double", "Double Sharing"),
    ]
    room_type = models.CharField(
        max_length=20,
        choices=ROOM_CHOICES,
        blank=True
    )

    # ================= MEALS =================
    meals_included = models.BooleanField(default=True)
    meal_plan = models.CharField(
        max_length=100,
        blank=True,
        help_text="Breakfast / Lunch / Dinner"
    )

    # ================= TOUR FEATURES =================
    sightseeing_included = models.BooleanField(default=True)
    tour_guide = models.BooleanField(default=True)

    # ================= PLACES COVERED =================
    places_covered = models.TextField(
        help_text="Comma separated places list",
        null=True,
        blank=True
    )

    # ================= OFFERS =================
    offer_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="Eg: Book 5 seats & get 5 bags free"
    )
    has_offer = models.BooleanField(default=False)

    # ================= MEDIA =================
    image = models.ImageField(
        upload_to="popular_packages/",
        null=True,
        blank=True
    )

    # ================= CTA CONTROL =================
    is_active = models.BooleanField(default=True)
    is_bookable = models.BooleanField(default=False)

    # ================= METADATA =================
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title