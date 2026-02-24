from django.urls import path
from . import views

urlpatterns = [
    # your mashimo routes will go here
]

from django.urls import path
from . import views

urlpatterns = [
    path('zones/', views.zones_map, name='zones_map'),
]