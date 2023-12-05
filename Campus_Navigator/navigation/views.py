import json
from django.shortcuts import render

from navigation.forms import LocationForm
from django.shortcuts import render, redirect
from .models import Location
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import CampusEvent, Building, Feedback
from .forms import BuildingForm  


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
    

@method_decorator(csrf_exempt, name='dispatch')
class CampusEventApiView(View):
    def get(self, request, *args, **kwargs):
        events = CampusEvent.objects.all()
        event_list = [{'id': event.id, 'campus_name': event.campus_name, 'event_name': event.event_name,
                       'event_description': event.event_description, 'event_image': event.event_image.url,
                       'event_timestamp': event.event_timestamp, 'slug': event.slug} for event in events]
        return JsonResponse({'events': event_list}, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        campus_event = CampusEvent.objects.create(
            campus_name=data['campus_name'],
            event_name=data['event_name'],
            event_description=data['event_description'],
            event_image=data['event_image'],
            event_timestamp=data['event_timestamp'],
            slug=data['slug']
        )
        return JsonResponse({'id': campus_event.id}, status=201)



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
