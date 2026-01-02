from django.contrib import admin
from .models import Package, PopularPackage


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active","price", "created_at")
    search_fields = ("title",)
    list_filter = ("is_active",)


@admin.register(PopularPackage)
class PopularPackageAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "price", "departure_date", "created_at")
    search_fields = ("title",)
    list_filter = ("is_active",)
