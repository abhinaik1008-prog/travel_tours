from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Package, PopularPackage
from .serializers import PackageSerializer, PopularPackageSerializer



# ================= HOME PAGE (HTML) =================
def home(request):
    return render(request, "home.html")




def packages_list(request):
    packages = Package.objects.filter(is_active=True)
    return render(request, "packages/packages_list.html", {
        "packages": packages
    })

def package_detail(request, id):
    package = get_object_or_404(Package, id=id, is_active=True)
    return render(request, "packages/package_detail.html", {
        "package": package
    })




# ================= NORMAL PACKAGES API (JSON) =================
class PackageListAPIView(ListAPIView):
    serializer_class = PackageSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Package.objects.filter(is_active=True)

        destination = self.request.query_params.get("destination")
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")
        duration = self.request.query_params.get("duration")

        if destination:
            queryset = queryset.filter(destination__name__icontains=destination)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if duration:
            queryset = queryset.filter(duration_days=duration)

        return queryset


class PackageDetailAPIView(RetrieveAPIView):
    queryset = Package.objects.filter(is_active=True)
    serializer_class = PackageSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"


# ================= POPULAR PACKAGES PAGE (HTML ONLY) =================
def popular_packages_page(request):
    """
    Renders HTML template.
    NO JSON
    NO API
    """
    packages = PopularPackage.objects.filter(is_active=True)

    return render(request, "popular_packages.html", {
        "packages": packages
    })


