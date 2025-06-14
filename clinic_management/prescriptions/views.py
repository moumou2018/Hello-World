from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Prescription
from django.db.models import Q

class PrescriptionListView(ListView):
    model = Prescription
    template_name = 'prescriptions/prescription_list.html'
    context_object_name = 'prescriptions'
    ordering = ['-start_date']

    def get_queryset(self):
        queryset = super().get_queryset().select_related('patient') # Optimize
        patient_query = self.request.GET.get('patient_name')
        medication_query = self.request.GET.get('medication_name')
        doctor_query = self.request.GET.get('doctor_name')

        if patient_query:
            queryset = queryset.filter(
                Q(patient__first_name__icontains=patient_query) | Q(patient__last_name__icontains=patient_query)
            )
        if medication_query:
            queryset = queryset.filter(medication_name__icontains=medication_query)
        if doctor_query:
            queryset = queryset.filter(issuing_doctor_name__icontains=doctor_query)
        return queryset

class PrescriptionDetailView(DetailView):
    model = Prescription
    template_name = 'prescriptions/prescription_detail.html'
    context_object_name = 'prescription'

class PrescriptionCreateView(CreateView):
    model = Prescription
    template_name = 'prescriptions/prescription_form.html'
    fields = ['patient', 'medication_name', 'dosage', 'frequency', 'start_date', 'end_date', 'issuing_doctor_name']
    success_url = reverse_lazy('prescriptions:prescription_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start_date'].widget.attrs.update({'placeholder': 'YYYY-MM-DD'})
        form.fields['end_date'].widget.attrs.update({'placeholder': 'YYYY-MM-DD'})
        return form

class PrescriptionUpdateView(UpdateView):
    model = Prescription
    template_name = 'prescriptions/prescription_form.html'
    fields = ['patient', 'medication_name', 'dosage', 'frequency', 'start_date', 'end_date', 'issuing_doctor_name']
    success_url = reverse_lazy('prescriptions:prescription_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start_date'].widget.attrs.update({'placeholder': 'YYYY-MM-DD'})
        form.fields['end_date'].widget.attrs.update({'placeholder': 'YYYY-MM-DD'})
        return form

class PrescriptionDeleteView(DeleteView):
    model = Prescription
    template_name = 'prescriptions/prescription_confirm_delete.html'
    success_url = reverse_lazy('prescriptions:prescription_list')
