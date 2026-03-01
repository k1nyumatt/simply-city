from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DropOffZone

def zones_map(request):
    zones = DropOffZone.objects.filter(is_active=True)
    return render(request, 'mashimo/map.html', {'zones': zones})

@login_required
def dashboard(request):
    zones = DropOffZone.objects.filter(is_active=True)
    return render(request, 'mashimo/dashboard.html', {'zones': zones, 'user': request.user})
