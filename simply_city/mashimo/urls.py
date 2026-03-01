from django.urls import path
from . import views

urlpatterns = [
    path('', views.zones_map, name='home'),
    path('zones/', views.zones_map, name='zones_map'),
]
