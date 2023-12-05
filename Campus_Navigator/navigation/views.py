import json
from django.shortcuts import render

from navigation.forms import LocationForm
from django.shortcuts import render, redirect
from .models import Location, SearchLocation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def get_locations(request):
    locations = Location.objects.all()
    data = [{'from_location': location.from_location, 'to_location': location.to_location,
             'timestamp': location.timestamp} for location in locations]
    return JsonResponse(data, safe=False)


@csrf_exempt
def add_location(request):
    if request.method == 'POST':
        print("API CALL RECEIVED")
        data = json.loads(request.body)
        print("data",data)
        # Access data from the payload
        from_location_data = data.get('from_location', {})
        to_location_data = data.get('to_location', {})
        travel_mode = data.get('travel_mode')
        search_by = data.get('search_by')

        from_location_name = from_location_data.get('name')
        from_location_lat = from_location_data.get('lat')
        from_location_lng = from_location_data.get('lng')

        to_location_name = to_location_data.get('name')
        to_location_lat = to_location_data.get('lat')
        to_location_lng = to_location_data.get('lng')

        if (
            from_location_name and from_location_lat and from_location_lng and
            to_location_name and to_location_lat and to_location_lng
        ):
            location = SearchLocation(
                from_location_name=from_location_name,
                from_location_lat=float(from_location_lat),
                from_location_lng=float(from_location_lng),
                to_location_name=to_location_name,
                to_location_lat=float(to_location_lat),
                to_location_lng=float(to_location_lng),
                travel_mode=travel_mode,
                search_by=search_by
            )
            print("location", location)
            location.save()
            return JsonResponse({'message': 'Location added successfully', 'status': 'success'})
        else:
            return JsonResponse({'error': 'Invalid data provided', 'status': 'fail'})
    else:
        return JsonResponse({'error': 'Invalid request method', 'status': 'fail'})
