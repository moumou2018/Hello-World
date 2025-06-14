from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Patient
from django.db.models import Q

class PatientListView(ListView):
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patients'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
        return queryset.order_by('last_name', 'first_name')

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patients/patient_detail.html'
    context_object_name = 'patient'

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'patients/patient_form.html'
    fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'address']
    success_url = reverse_lazy('patients:patient_list')

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patients/patient_form.html'
    fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'address']
    success_url = reverse_lazy('patients:patient_list')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patients/patient_confirm_delete.html'
    success_url = reverse_lazy('patients:patient_list')
