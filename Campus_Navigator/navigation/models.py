from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Location(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_location} to {self.to_location} at {self.timestamp}"


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