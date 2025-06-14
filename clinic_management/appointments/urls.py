from django.urls import path
from .views import (
    AppointmentListView,
    AppointmentDetailView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView
)

app_name = 'appointments'
urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment_list'),
    path('<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('new/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
]
