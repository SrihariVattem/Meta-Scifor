from django.db import models
from django.contrib.auth.models import User


# Event Category Model
class EventCategory(models.Model):
    name = models.CharField(max_length=50,)

    def __str__(self):
        return self.name


# Event Model
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    # Setting default category
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='events',)  # Use a valid ID here

    def __str__(self):
        return self.title


# Registration Model
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    description = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"
