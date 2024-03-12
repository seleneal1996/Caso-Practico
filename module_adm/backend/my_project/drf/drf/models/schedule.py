from django.db import models
from .staff import Collaborator

class Schedule(models.Model):
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    day_of_the_week = models.CharField(max_length=20)
    start_time=models.TimeField()
    end_time= models.TimeField()