from django.contrib import admin
from .models import (
    Destination, 
    Package, 
    PackageImage, 
    Availability, 
    PopularPackage
)

# Register your models here.
class PackageImageInline(admin.TabularInline):
    model = PackageImage
    extra = 1


class AvailabilityInline(admin.TabularInline):
    model = Availability
    extra = 1


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'price', 'duration_days', 'is_active')
    list_filter = ('destination', 'is_active')
    search_fields = ('title',)
    inlines = [PackageImageInline, AvailabilityInline]
    list_editable = ('is_active',)


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    search_fields = ('name', 'country')


admin.site.register(PackageImage)
admin.site.register(Availability)


@admin.register(PopularPackage)
class PopularPackageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "region",
        "price",
        "rating",
        "reviews_count",
        "is_active",
        "is_bookable"
    )
    list_filter = ("region", "is_active", "is_bookable")
    search_fields = ("title", "description")
