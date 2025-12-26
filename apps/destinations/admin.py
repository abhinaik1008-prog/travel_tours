from django.contrib import admin
from .models import Destination

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'is_active')
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('is_featured', 'is_active')
    search_fields = ('name',)
