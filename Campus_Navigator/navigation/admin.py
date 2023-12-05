from django.contrib import admin

from .models import Location, SearchLocation
from .models import Location, CampusEvent, Building, Feedback

# Register your models here.


admin.site.register(Location)
admin.site.register(SearchLocation)

class CampusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("event_name",)}

admin.site.register(CampusEvent,CampusAdmin)

admin.site.register(Building)
admin.site.register(Feedback)
