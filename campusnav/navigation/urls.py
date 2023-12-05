from django.urls import path,include

from . import views

urlpatterns = [
    path('api/get_locations', views.get_locations, name='get_locations'),
    path('api/add_locations', views.add_location, name='add_location'),
]
