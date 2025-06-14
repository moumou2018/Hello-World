from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Appointment
from patients.models import Patient # Needed for Create/Update forms if selecting patient
from django.db.models import Q

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'
    ordering = ['-appointment_date'] # Show newest first

    def get_queryset(self):
        queryset = super().get_queryset().select_related('patient') # Optimize by selecting related patient
        patient_query = self.request.GET.get('patient_name')
        doctor_query = self.request.GET.get('doctor_name')
        status_query = self.request.GET.get('status')

        if patient_query:
            queryset = queryset.filter(
                Q(patient__first_name__icontains=patient_query) | Q(patient__last_name__icontains=patient_query)
            )
        if doctor_query:
            queryset = queryset.filter(doctor_name__icontains=doctor_query)
        if status_query:
            queryset = queryset.filter(status__iexact=status_query)
        return queryset

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

class AppointmentCreateView(CreateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['patient', 'doctor_name', 'appointment_date', 'reason', 'status']
    success_url = reverse_lazy('appointments:appointment_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['appointment_date'].widget.attrs.update({'placeholder': 'YYYY-MM-DD HH:MM:SS'})
        return form

class AppointmentUpdateView(UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['patient', 'doctor_name', 'appointment_date', 'reason', 'status']
    success_url = reverse_lazy('appointments:appointment_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['appointment_date'].widget.attrs.update({'placeholder': 'YYYY-MM-DD HH:MM:SS'})
        return form

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointments/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointments:appointment_list')
