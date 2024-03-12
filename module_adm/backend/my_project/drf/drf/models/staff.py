#Personal

from django.db import models

class Collaborator(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_of_birth = models.DateField()

class Contact(models.Model):
    collaborator =models.ForeignKey(Collaborator,on_delete= models.CASCADE)
    type = models.CharField(max_length=50)
    value = models.CharField(max_length=100)