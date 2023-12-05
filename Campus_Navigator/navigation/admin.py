from django.contrib import admin

from .models import Location
from .models import CampusEvent

# Register your models here.


admin.site.register(Location)
# admin.site.register(CampusEvent)

class CampusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("event_name",)}

admin.site.register(CampusEvent,CampusAdmin)





