from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Location(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_location} to {self.to_location} at {self.timestamp}"
    
class SearchLocation(models.Model):
    TRAVEL_MODE_CHOICES = [
        ('WALKING', 'Walking'),
        ('DRIVING', 'Driving'),
        ('CYCLING', 'Cycling'),
    ]
    from_location_name = models.CharField(max_length=100)
    from_location_lat = models.FloatField()
    from_location_lng = models.FloatField()
    to_location_name = models.CharField(max_length=100)
    to_location_lat = models.FloatField()
    to_location_lng = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    travel_mode = models.CharField(max_length=10, choices=TRAVEL_MODE_CHOICES)
    search_by = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.from_location_name} to {self.to_location_name} at {self.timestamp}"
    

class CampusEvent(models.Model):
    campus_name = models.CharField(max_length=100)
    event_id = models.CharField(max_length=50, unique=True)  # Assuming event_id is a unique identifier
    event_name = models.CharField(max_length=200)
    event_description = models.TextField()
    event_image = models.ImageField(upload_to='event_images/')  # Adjust the upload_to path as needed
    event_timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically generate a slug from the event name
        self.slug = slugify(self.event_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.event_name} at {self.campus_name} on {self.event_timestamp}"

class Building(models.Model):
    build_name = models.CharField(max_length=100)
    build_img = models.ImageField(_("Building Image"), upload_to='building_images/', height_field=None, width_field=None, max_length=None)
    build_description = models.TextField()

    def __str__(self):
        return self.build_name


class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    admin_comment = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}'s Feedback"
