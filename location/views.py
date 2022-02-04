from rest_framework import generics
from .models import Hotel,Location,HotelTwoT,points
from rest_framework.generics import GenericAPIView
from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim
from .serializers import *#HotelSerializer,HotelTwoSerializer,HotelGetSerializer,HotelTwoGetSerializer
from rest_framework.response import Response
geolocator = Nominatim(user_agent="location")
from django.contrib.gis.geos import Point

from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.gis.db.models.functions import Distance


from location.serializers import *
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
    queryset = HotelTwoT.objects.all()
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
    serializer_class = HotelTwoSerializer
    queryset = HotelTwoT.objects.select_related()
    # def get(self,request):
    #     try:
    #         query_set = self.get_queryset()
    #         serializer = HotelTwoGetSerializer(query_set,many=True)    
    #         msg = "your data"
    #         return Response({"data":serializer.data,"msg":msg})
    #     except Exception as e:
    #         return Response({"error":str(e)})
        
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


@csrf_exempt
def addpoint(request):
    if request.method =='POST':
        name=request.POST['name']
        lat=float(request.POST['latitude'])
        long=float(request.POST['longitude'])
        desc=request.POST['description']
        location=Point(long,lat,srid=4326)
        newpoint = points(name=name,location=location,description=desc)
        newpoint.save()
        
    return render(request,'addpoint.html')

@csrf_exempt
def viewpoints(request):
    if request.method=='POST':
        lat1=float(request.POST['latitude'])
        long1=float(request.POST['longitude'])
        user_location = Point(long1,lat1,srid=4326)
        queryset = points.objects.annotate(distance=Distance("location", user_location)).order_by("distance")[0:1]    
        names=[i for i in queryset]
        name=[i.name for i in names]
        lo=[i.location for i in names]
        xy=[[j for j in i] for i in lo]
        lat=[i[1] for i in xy]
        long=[i[0] for i in xy]
        return render(request,'showpoints.html',{'allpoints':queryset,'name':name,'lat':lat,'long':long})
    return render(request,'map.html')


def allpoints(request):
    allpoints=points.objects.all()
    names=[i for i in allpoints]
    name=[i.name for i in names]
    lo=[i.location for i in names]
    xy=[[j for j in i] for i in lo]
    lat=[i[1] for i in xy]
    long=[i[0] for i in xy]
    return render(request,'allpoints.html',{'allpoints':allpoints,'name':name,'lat':lat,'long':long})
