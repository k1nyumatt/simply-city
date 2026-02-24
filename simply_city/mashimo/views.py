from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import DropOffZone

def zones_map(request):
    zones = DropOffZone.objects.filter(is_active=True)
    return render(request, 'mashimo/map.html', {'zones': zones})