from django.db import models
from appointments.models import Appointment

class Consultation(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='consultation')
    notes = models.TextField()
    diagnosis = models.TextField()
    treatment_plan = models.TextField()

    def __str__(self):
        return f"Consultation for {self.appointment}"
