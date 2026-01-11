from django.urls import path
from .views import home, packages_page

urlpatterns = [
    path("", home, name="home"),
    path("packages/", packages_page, name="packages"),
]
