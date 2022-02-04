from location.models import Hotel, HotelTwoT
from rest_framework import serializers


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel

        fields = ("id", "name", "address", "location")

        extra_kwargs = {"location": {"read_only": True}}
class HotelGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel

        fields = ("id", "name","address")

class HotelTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelTwoT

        fields = ("id","name","street_1","street_2","city","state","zip_code","country","location")
        extra_kwargs = {"location": {"read_only": True}}
class HotelTwoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelTwoT

        fields = ("id","name","zip_code",)