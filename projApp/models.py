from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    d_o_b = models.DateField()
    diagnosed_disease = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.user)

class Physician(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    specialty = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.user)

class Schedule(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Physician, on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField()

    def __str__(self):
        return str(f'{self.doctor}/{self.patient}\'s appointment')

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

class DeviceData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    data_type = models.CharField(max_length = 50)
    value = models.FloatField()

    def __str__(self):
        return str(f'{self.patient}\'s {self.data_type} result')

class Consultation(models.Model):
    appointment = models.OneToOneField(Schedule, on_delete=models.CASCADE)
    virtual_consultation_link = models.URLField()

    def __str__(self):
        return str(self.appointment)
