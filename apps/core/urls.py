from django.urls import path
from . import views

urlpatterns = [
    path("create-admin/", views.create_admin),
    path('', views.home, name='home'),
    path('destinations/', views.destinations, name='destinations'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
