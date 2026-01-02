from django.urls import path
from .views import (
    home,
    PackageListAPIView,
    PackageDetailAPIView,
    popular_packages_page,
    package_detail,
    packages_list
)

urlpatterns = [
    # HTML pages
    path("", home, name="home"),
    path("popular-packages/", popular_packages_page, name="popular-packages-page"),

    # APIs (prefix with api/)
    path("api/packages/", PackageListAPIView.as_view(), name="packages-api"),
    path("api/packages/<int:id>/", PackageDetailAPIView.as_view(), name="package-detail-api"),

    path("", packages_list, name="packages"),
    path("<int:id>/", package_detail, name="package-detail"),
]
