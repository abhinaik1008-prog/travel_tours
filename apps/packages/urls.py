from django.urls import path
from .views import (
    home,
    PackageListAPIView,
    PackageDetailAPIView,
    popular_packages_page
)

urlpatterns = [
    # HTML pages
    path("", home, name="home"),
    path("popular-packages/", popular_packages_page, name="popular-packages-page"),

    # APIs (prefix with api/)
    path("api/packages/", PackageListAPIView.as_view(), name="packages-api"),
    path("api/packages/<int:pk>/", PackageDetailAPIView.as_view(), name="package-detail-api"),
]
