from django.urls import path
from .views import (
    ConsultationListView,
    ConsultationDetailView,
    ConsultationCreateView,
    ConsultationUpdateView,
    ConsultationDeleteView
)

app_name = 'consultations'
urlpatterns = [
    path('', ConsultationListView.as_view(), name='consultation_list'),
    path('<int:pk>/', ConsultationDetailView.as_view(), name='consultation_detail'),
    path('new/', ConsultationCreateView.as_view(), name='consultation_create'),
    path('<int:pk>/edit/', ConsultationUpdateView.as_view(), name='consultation_update'),
    path('<int:pk>/delete/', ConsultationDeleteView.as_view(), name='consultation_delete'),
]
