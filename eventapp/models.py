from django.db import models

class Event(models.Model):
    event_title = models.CharField(max_length=120)
    location = models.CharField(max_length=70)
    event_date = models.CharField(max_length=120)
    description = models.TextField()

    def _str_(self):
        return self.event_title

class data(models.Model):
    name = models.CharField(max_length = 100 )
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)
    event = models.ForeignKey('Event',on_delete=models.CASCADE)

    def _str_(self):
        return self.name
