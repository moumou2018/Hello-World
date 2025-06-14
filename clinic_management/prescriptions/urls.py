from django.urls import path
from .views import (
    PrescriptionListView,
    PrescriptionDetailView,
    PrescriptionCreateView,
    PrescriptionUpdateView,
    PrescriptionDeleteView
)

app_name = 'prescriptions'
urlpatterns = [
    path('', PrescriptionListView.as_view(), name='prescription_list'),
    path('<int:pk>/', PrescriptionDetailView.as_view(), name='prescription_detail'),
    path('new/', PrescriptionCreateView.as_view(), name='prescription_create'),
    path('<int:pk>/edit/', PrescriptionUpdateView.as_view(), name='prescription_update'),
    path('<int:pk>/delete/', PrescriptionDeleteView.as_view(), name='prescription_delete'),
]
