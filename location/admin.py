from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Hotel,Location,HotelTwo


@admin.register(Hotel)
class HotelAdmin(LeafletGeoAdmin):
    list_display = ("id", "name", "address", "location", "created_at", "updated_at")


@admin.register(Location)
class LocationAdmin(LeafletGeoAdmin):
    list_display = ("id", "name",  "location")

@admin.register(HotelTwo)
class HotelTwoAdmin(LeafletGeoAdmin):
    list_display = ("id", "name", "street_1", "street_2", "city", "state", "zip_code", "country", "location", "created_at", "updated_at")