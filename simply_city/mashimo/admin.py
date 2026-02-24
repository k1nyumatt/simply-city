from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DropOffZone

@admin.register(DropOffZone)
class DropOffZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')