import os
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from apps.destinations.models import Destination
from apps.packages.models import PopularPackage
from django.contrib.staticfiles import finders

def health_check(request):
    return HttpResponse("Travel & Tours is LIVE 🚀")

def home(request):
    destinations = Destination.objects.filter(is_active=True)[:6]
    popular_packages = PopularPackage.objects.filter(is_active=True)[:6]

    # ================= MEMORIES (DYNAMIC) =================
    memories_dir = os.path.join(settings.STATICFILES_DIRS[0], "images/memories")

    memories = []

    memories_dir = finders.find("images/memories")
    if memories_dir:
        memories = sorted(
            [
                f"images/memories/{img}"
                for img in os.listdir(memories_dir)
                if img.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
            ]
        )


        return render(request, 'home/home.html', {
            'destinations': destinations,
            'popular_packages': popular_packages,
            'memories': memories,   # ✅ added safely
        })


def about(request):
    return render(request, 'about/about.html', {"hide_footer": True})

def destinations(request):
    destinations = Destination.objects.filter(is_active=True)

    return render(request, 'destinations/destinations.html', {
        'destinations': destinations,
        'hide_footer': True
    })

def packages(request):
    return render(request, 'packages/packages.html', {"hide_footer": True})

def contact(request):
    return render(request, 'contact/contact.html', {"hide_footer": True})
