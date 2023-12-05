from django.db import models

# Create your models here.

class Location(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_location} to {self.to_location} at {self.timestamp}"