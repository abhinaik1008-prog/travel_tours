from django.urls import path
from .views import packages_page

urlpatterns = [
    path("", packages_page, name="packages"),
]
