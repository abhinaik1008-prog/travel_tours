from django.shortcuts import render
from .models import PopularPackage

def home(request):
    popular_packages = PopularPackage.objects.filter(is_active=True)[:6]
    return render(request, "home/home.html", {
        "popular_packages": popular_packages
    })


# ================= PACKAGES PAGE ================
def packages_page(request):
    packages = PopularPackage.objects.filter(is_active=True)
    return render(request, 'packages/packages.html', {
        'packages': packages,
        "hide_footer": True
    })