# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .serializers import *
from .models import *


# class HomeView(TemplateView):
#     template_name = 'hello.html'


# class HomeLoginView(LoginRequiredMixin, TemplateView):
#     template_name = 'hellologin.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["doctors"] = DoctorName.objects.all()
#         context["specializations"] = DoctorType.objects.all()
#         context["appointments"] = AppointmentDates.objects.all()
#         return context

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class AppointmentDateCrudViewSet(viewsets.ModelViewSet):
    """
    (C)reate (R)ead (U)date (D)elete actions.
    """
    queryset = AppointmentDates.objects.all()
    serializer_class = AppointmentDatesSerializer
    permission_classes = [permissions.IsAuthenticated] # tylko zalogowani będą mieć dostęp (możesz też zmienić w settings dla całego projektu)


class DoctorNameCrudViewSet(viewsets.ModelViewSet):
    """
    (C)reate (R)ead (U)date (D)elete actions.
    """
    queryset = DoctorName.objects.all()
    serializer_class = DoctorNameSerializer
    permission_classes = [IsSuperUser]


class DoctorTypeCrudViewSet(viewsets.ModelViewSet):
    """
    (C)reate (R)ead (U)date (D)elete actions.
    """
    queryset = DoctorType.objects.all()
    serializer_class = DoctorTypeSerializer
    permission_classes = [IsSuperUser]







# Na daną chwilę nie jest nam potrzebne, przyda się jednak w przyszłości - widok na read only
# class DataViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     Read only view.
#     """
#     queryset = DoctorType.objects.all()
#     serializer_class = DoctorTypeSerializer




