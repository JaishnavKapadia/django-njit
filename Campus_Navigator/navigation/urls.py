from django.urls import path,include

from . import views

urlpatterns = [
    path('api/get_locations', views.get_locations, name='get_locations'),
    path('api/add_locations', views.add_location, name='add_location'),
    path('api/get_campus_events/', views.CampusEventApiView.as_view(), name='get_campus_events'),
    path('api/get_buildings/', views.get_buildings, name='get_buildings'),
    path('api/add_building/', views.add_building, name='add_building'),

    path('api/get_feedback/', views.get_buildings, name='get_buildings'),
    path('api/get_feedback_byID/', views.add_building, name='add_building'),
    path('api/save_admin_comment/', views.get_buildings, name='get_buildings'),

]
