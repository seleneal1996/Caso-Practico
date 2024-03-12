from django.db import models

class Collaborator(models.Model):
    id_colaborador = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.CharField(max_length=15)
    estado = models.CharField(max_length=10, choices=[('activo', 'activo'), ('inactivo', 'inactivo')], default='activo')

class ContractType(models.Model):
    name = models.CharField(max_length=255)
    eps = models.BooleanField()
    insurance = models.BooleanField()

class Contact(models.Model):
    id_collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=10, choices=[('phone', 'phone'), ('email', 'email')])
    contact_detail = models.CharField(max_length=255)

class Contract(models.Model):
    id_collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    id_contract_type = models.ForeignKey(ContractType, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)

class Schedule(models.Model):
    id_collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday'), ('sunday', 'sunday')])
    start_time = models.TimeField()
    end_time = models.TimeField()

class Assignment(models.Model):
    id_contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    id_schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)  # Las contraseñas deben almacenarse de forma segura utilizando funciones de hash
    role = models.CharField(max_length=15, choices=[('administrator', 'administrator'), ('user', 'user')], default='user')
    id_collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
