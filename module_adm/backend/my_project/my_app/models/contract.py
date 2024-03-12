from django.db import models
from .staff import Collaborator

class Contract(models.Model):
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    eps = models.CharField(max_length=50)
    life_insurance = models.CharField(max_length=50)