from django.db import models

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
    