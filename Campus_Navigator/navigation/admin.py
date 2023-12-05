from django.contrib import admin

from .models import Location,Building,Feedback

# Register your models here.


admin.site.register(Location)
admin.site.register(Building)
admin.site.register(Feedback)