from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'package',
        'travel_date',
        'number_of_people',
        'total_price',
        'status',
        'created_at',
    )
    list_filter = ('status', 'travel_date')
    search_fields = ('user__phone', 'package__title')
    list_editable = ('status',)
