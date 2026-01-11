from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destinations, name='destinations'),
    path('packages/', views.packages, name='packages'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
