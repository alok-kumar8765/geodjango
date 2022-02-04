from re import I
from django.urls import path
from .views import HotelUpdateRetreiveView, ListCreateGenericViews, addpoint, allpoints,index, viewpoints,HotelCreateAPIView,ListCreateGenericAPIViews,DetaileHotelApiView

urlpatterns = [
    path("hotels/", ListCreateGenericViews.as_view()),
    path("hotels/<str:pk>/",HotelUpdateRetreiveView.as_view()),
    path('index/', index, name='index'),
    path('hotel/', HotelCreateAPIView.as_view(), name='hotel'),
    path("hotel2/",ListCreateGenericAPIViews.as_view()),
    path('detail/',DetaileHotelApiView.as_view(),name='detail'),
    path('addlocation',addpoint,name='addpoint'),
    path('viewpoints',viewpoints,name='viewpoints'),
    path('allpoints',allpoints,name='allpoints'),
]