import json
from django.shortcuts import render

from navigation.forms import LocationForm
from django.shortcuts import render, redirect
from .models import Location
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def get_locations(request):
    locations = Location.objects.all()
    data = [{'from_location': location.from_location, 'to_location': location.to_location, 'timestamp': location.timestamp} for location in locations]
    return JsonResponse(data, safe=False)
    
@csrf_exempt
def add_location(request):
    if request.method == 'POST':
        print("API CALL RECICVED")
        data = json.loads(request.body)
        from_location = data.get('from_location')
        to_location = data.get('to_location')

        if from_location and to_location:
            location = Location(from_location=from_location, to_location=to_location)
            location.save()
            return JsonResponse({'message': 'Location added successfully','status':'success'})
        else:
            return JsonResponse({'error': 'Invalid data provided','status':'fail'})
    else:
        return JsonResponse({'error': 'Invalid request method','status':'fail'})