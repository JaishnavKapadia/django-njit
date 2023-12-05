from django.contrib import admin

from .models import Location, SearchLocation

# Register your models here.


admin.site.register(Location)
admin.site.register(SearchLocation)