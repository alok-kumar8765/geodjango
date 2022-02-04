from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import *


@admin.register(Hotel)
class HotelAdmin(LeafletGeoAdmin):
    list_display = ("id", "name", "address", "location", "created_at", "updated_at")


@admin.register(Location)
class LocationAdmin(LeafletGeoAdmin):
    list_display = ("id", "name",  "location")

@admin.register(HotelTwoT)
class HotelTwoAdmin(LeafletGeoAdmin):
    list_display = ("id", "name",  "city",)
    

class Points(LeafletGeoAdmin):
    list_display = ("id", "name", "description")
admin.register(points,Points)

admin.site.register(NairobiHealthFacilities)
# class NairobiHealthFacilitiesAdmin(LeafletGeoAdmin):
#     list_display = ("id", "name", "addr_city", "addr_street", "contact_phone")

admin.site.register(NairobiSubCounties)