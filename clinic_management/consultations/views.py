from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Consultation
from appointments.models import Appointment # Needed for form

class ConsultationListView(ListView):
    model = Consultation
    template_name = 'consultations/consultation_list.html'
    context_object_name = 'consultations'
    # Consider ordering by appointment date via related field
    # ordering = ['-appointment__appointment_date']

class ConsultationDetailView(DetailView):
    model = Consultation
    template_name = 'consultations/consultation_detail.html'
    context_object_name = 'consultation'

class ConsultationCreateView(CreateView):
    model = Consultation
    template_name = 'consultations/consultation_form.html'
    fields = ['appointment', 'notes', 'diagnosis', 'treatment_plan']
    success_url = reverse_lazy('consultations:consultation_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Optional: Filter appointments that don't have a consultation yet
        # form.fields['appointment'].queryset = Appointment.objects.filter(consultation__isnull=True)
        return form


class ConsultationUpdateView(UpdateView):
    model = Consultation
    template_name = 'consultations/consultation_form.html'
    fields = ['appointment', 'notes', 'diagnosis', 'treatment_plan']
    success_url = reverse_lazy('consultations:consultation_list')

class ConsultationDeleteView(DeleteView):
    model = Consultation
    template_name = 'consultations/consultation_confirm_delete.html'
    success_url = reverse_lazy('consultations:consultation_list')
