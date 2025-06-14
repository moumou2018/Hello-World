from django.db import models
from patients.models import Patient

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) # End date might not always be there
    issuing_doctor_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Prescription for {self.patient} - {self.medication_name}"
