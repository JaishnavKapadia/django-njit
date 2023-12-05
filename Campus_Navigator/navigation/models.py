from django.db import models
from django.utils.text import slugify

# Create your models here.

class Location(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_location} to {self.to_location} at {self.timestamp}"

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
