from rest_framework import generics
from .models import Hotel,Location,HotelTwo
from rest_framework.generics import GenericAPIView
from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim
from .serializers import HotelSerializer,HotelTwoSerializer,HotelGetSerializer
from rest_framework.response import Response
geolocator = Nominatim(user_agent="location")

from location.serializers import HotelSerializer
from django.shortcuts import render


class ListCreateGenericViews(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_create(self, serializer):
        address = serializer.initial_data["address"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)

class HotelCreateAPIView(GenericAPIView):
    serializer_class = HotelGetSerializer
    queryset = Hotel.objects.select_related()
    def get(self,request):
        try:
            query_set = self.get_queryset()
            serializer = HotelGetSerializer(query_set,many=True)
            msg = "your data"
            return Response({"data":serializer.data,"msg":msg})
        except Exception as e:
            return Response({"error":str(e)})
    def post(self,request):
        try:
            serializer = HotelSerializer(data=request.data)
            if serializer.is_valid():
                address = serializer.initial_data["address"]
                g = geolocator.geocode(address)
                lat = g.latitude
                lng = g.longitude
                pnt = Point(lng, lat)
                serializer.save(location=pnt)
                return Response({"data":serializer.data,"msg":"your data"})
            else:
                return Response({"error":serializer.errors})
        except Exception as e:
            return Response({"error":str(e)})
    def delete(self,request):
        try:
            query_set = self.get_queryset()
            query_set.delete()
            return Response({"msg":"your data deleted"})
        except Exception as e:
            return Response({"error":str(e)})
        
class HotelUpdateRetreiveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_update(self, serializer):
        address = serializer.initial_data["address"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)
        
def index(request):
    locations = Location.objects.all()
    return render(request, 'index.html', {'locations': locations})

class ListCreateGenericAPIViews(generics.ListCreateAPIView):
    queryset = HotelTwo.objects.all()
    serializer_class = HotelTwoSerializer

    def perform_create(self, serializer):
        street_1 = serializer.initial_data["street_1"]
        address = serializer.initial_data["city"]
        state = serializer.initial_data["state"]
        country = serializer.initial_data["city"]
        data = [street_1, address, state, country]
        " ".join(data)

        g = geolocator.geocode(data)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)
class DetaileHotelApiView(GenericAPIView):
    serializer_class = HotelGetSerializer
    queryset = HotelTwo.objects.select_related()
    def get(self,request):
        try:
            query_set = self.get_queryset()
            serializer = HotelGetSerializer(query_set,many=True)
    
            msg = "your data"
            return Response({"data":serializer.data,"msg":msg})
        except Exception as e:
            return Response({"error":str(e)})
    def post(self,request):
        try:
            serializer = HotelTwoSerializer(data=request.data)
            if serializer.is_valid():
                street_1 = serializer.initial_data["street_1"]
                address = serializer.initial_data["city"]
                state = serializer.initial_data["state"]
                country = serializer.initial_data["city"]
                data = [street_1, address, state, country]
                " ".join(data)

                g = geolocator.geocode(data)
                lat = g.latitude
                lng = g.longitude
                pnt = Point(lng, lat)
                print(pnt)
                serializer.save(location=pnt)  
                return Response({"data":serializer.data,"msg":"your data"})    
            else:
                return Response({"error":serializer.errors})
        except Exception as e:
            return Response({"error":str(e)})

# class HotelUpdateRetreiveView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelSerializer

#     def perform_update(self, serializer):
#         street_1 = serializer.initial_data["street_1"]
#         address = serializer.initial_data["city"]
#         state = serializer.initial_data["state"]
#         country = serializer.initial_data["city"]
#         data = [street_1, address, state, country]
#         " ".join(data)

#         g = geolocator.geocode(data)
#         lat = g.latitude
#         lng = g.longitude
#         pnt = Point(lng, lat)
#         print(pnt)
#         serializer.save(location=pnt)