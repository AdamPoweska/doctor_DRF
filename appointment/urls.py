from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'doctor_type_crud_view_set', views.DoctorTypeCrudViewSet, basename='doctortype')
router.register(r'doctor_name_crud_view_set', views.DoctorNameCrudViewSet, basename='doctor_name_crud_view_set')
router.register(r'appointment_date_crud_view_set', views.AppointmentDateCrudViewSet, basename='appointment_date_crud_view_set')

urlpatterns = [
    path('', include(router.urls)),
]
