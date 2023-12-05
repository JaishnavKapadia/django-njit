from django.urls import path,include

from . import views

urlpatterns = [
    path('api/get_locations', views.get_locations, name='get_locations'),
    path('api/add_locations', views.add_location, name='add_location'),
    path('api/get_campus_events/', views.CampusEventApiView.as_view(), name='get_campus_events'),
]