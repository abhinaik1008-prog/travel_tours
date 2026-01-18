from django.contrib import admin
from .models import PopularPackage


@admin.register(PopularPackage)
class PopularPackageAdmin(admin.ModelAdmin):
    list_display = ("title", "region", "price", 'has_offer', "is_active", "is_bookable")
    list_filter = ("region", "is_active", "is_bookable")
    search_fields = ("title", "region")
