from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'is_staff', 'is_active')
    search_fields = ('phone',)
