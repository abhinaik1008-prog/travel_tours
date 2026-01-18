from django.shortcuts import render
from .models import PopularPackage

# ================= PACKAGES PAGE ================
def packages_page(request):
    packages = PopularPackage.objects.filter(is_active=True)
    return render(request, 'packages/packages.html', {
        'packages': packages,
        "hide_footer": True
    })