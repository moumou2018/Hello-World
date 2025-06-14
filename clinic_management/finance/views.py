from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Invoice
from django.db.models import Q

class InvoiceListView(ListView):
    model = Invoice
    template_name = 'finance/invoice_list.html'
    context_object_name = 'invoices'
    ordering = ['-issued_date']

    def get_queryset(self):
        queryset = super().get_queryset().select_related('patient') # Optimize
        patient_query = self.request.GET.get('patient_name')
        payment_status_query = self.request.GET.get('payment_status')

        if patient_query:
            queryset = queryset.filter(
                Q(patient__first_name__icontains=patient_query) | Q(patient__last_name__icontains=patient_query)
            )
        if payment_status_query:
            queryset = queryset.filter(payment_status__iexact=payment_status_query)
        return queryset

    def get_context_data(self, **kwargs): # Add choices to context for the template
        context = super().get_context_data(**kwargs)
        context['payment_status_choices'] = Invoice.PAYMENT_STATUS_CHOICES
        return context

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'finance/invoice_detail.html'
    context_object_name = 'invoice'

class InvoiceCreateView(CreateView):
    model = Invoice
    template_name = 'finance/invoice_form.html'
    fields = ['patient', 'appointment', 'service_description', 'amount', 'payment_status']
    success_url = reverse_lazy('finance:invoice_list')

class InvoiceUpdateView(UpdateView):
    model = Invoice
    template_name = 'finance/invoice_form.html'
    fields = ['patient', 'appointment', 'service_description', 'amount', 'payment_status']
    success_url = reverse_lazy('finance:invoice_list')

class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'finance/invoice_confirm_delete.html'
    success_url = reverse_lazy('finance:invoice_list')
