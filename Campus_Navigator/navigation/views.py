import json
from django.shortcuts import render

from navigation.forms import LocationForm
from django.shortcuts import render, redirect
from .models import Location
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import BuildingForm  
from .models import Building,Feedback


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



@csrf_exempt
def get_buildings(request):
    buildings = Building.objects.all()
    data = [{'build_name': building.build_name, 'build_img': building.build_img.url, 'build_description': building.build_description} for building in buildings]
    return JsonResponse(data, safe=False)

@csrf_exempt
def add_building(request):
    if request.method == 'POST':
        print("API CALL RECEIVED")
        data = json.loads(request.body)
        build_name = data.get('build_name')
        build_img = data.get('build_img')
        build_description = data.get('build_description')

        if build_name and build_img and build_description:
            building = Building(build_name=build_name, build_img=build_img, build_description=build_description)
            building.save()
            return JsonResponse({'message': 'Building added successfully', 'status': 'success'})
        else:
            return JsonResponse({'error': 'Invalid data provided', 'status': 'fail'})
    else:
        return JsonResponse({'error': 'Invalid request method', 'status': 'fail'})


@csrf_exempt
def get_feedback(request):
    feedback_list = Feedback.objects.all()
    data = [{'user_name': feedback.user_name, 'comment': feedback.comment, 'timestamp': feedback.timestamp} for feedback in feedback_list]
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_feedback_by_id(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        feedback_id = data.get('feedback_id')

        if feedback_id:
            feedback = Feedback.objects.get(pk=feedback_id)
            return JsonResponse({'user_name': feedback.user_name, 'comment': feedback.comment, 'timestamp': feedback.timestamp})
        else:
            return JsonResponse({'error': 'Invalid data provided', 'status': 'fail'})
    else:
        return JsonResponse({'error': 'Invalid request method', 'status': 'fail'})

@csrf_exempt
def save_admin_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        feedback_id = data.get('feedback_id')
        admin_comment = data.get('admin_comment')

        if feedback_id and admin_comment:
            feedback = Feedback.objects.get(pk=feedback_id)
            feedback.admin_comment = admin_comment
            feedback.save()
            return JsonResponse({'message': 'Admin comment saved successfully', 'status': 'success'})
        else:
            return JsonResponse({'error': 'Invalid data provided', 'status': 'fail'})
    else:
        return JsonResponse({'error': 'Invalid request method', 'status': 'fail'})