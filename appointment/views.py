# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .serializers import *
from .models import *


class IsReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: 
            return True
        elif request.user and request.user.is_staff: 
            return True
        

class AppointmentDateCrudViewSet(viewsets.ModelViewSet):
    """
    (C)reate (R)ead (U)date (D)elete actions.
    """
    queryset = AppointmentDates.objects.all()
    serializer_class = AppointmentDatesSerializer
    permission_classes = [permissions.IsAuthenticated]


class DoctorNameCrudViewSet(viewsets.ModelViewSet):
    """
    (C)reate (R)ead (U)date (D)elete actions.
    """
    queryset = DoctorName.objects.all()
    serializer_class = DoctorNameSerializer
    permission_classes = [IsReadOnly]


class DoctorTypeViewSet(viewsets.ModelViewSet):
    queryset = DoctorType.objects.all()
    serializer_class = DoctorTypeSerializer
    permission_classes = [IsReadOnly]


class DoctorNameNestedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DoctorNameNestedSerializer

    def get_queryset(self):
        return DoctorName.objects.filter(main_specialization_id=self.kwargs['doctor_type_pk'])


class AppointmentNestedViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentDatesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AppointmentDates.objects.filter(doctor_id=self.kwargs['doctor_pk'])
    
    def perform_create(self, serializer):
        doctor = DoctorName.objects.get(pk=self.kwargs['doctor_pk'])
        serializer.save(doctor=doctor)
