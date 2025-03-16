# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

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


class IsReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # safe_methods to GET', 'HEAD', 'OPTIONS' - czyli do tego moga miec dostep wszycy
            return True
        elif request.user and request.user.is_staff: # jesli nie sa to safe methods ale uzytkownik jest zalogowany i jest adminem
            return True
        

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
    permission_classes = [IsReadOnly]


class DoctorTypeCrudViewSet(viewsets.ModelViewSet):
    """
    (C)reate (R)ead (U)date (D)elete actions.
    """
    queryset = DoctorType.objects.all()
    serializer_class = DoctorTypeSerializer
    permission_classes = [IsReadOnly]


class DoctorTypeViewSet(viewsets.ModelViewSet):
    queryset = DoctorType.objects.all()
    serializer_class = DoctorTypeSerializer
    permission_classes = [IsReadOnly]

    # /doctor_types/<id>/doctors/
    @action(detail=True, methods=['get'])
    def doctors(self, request, pk=None):
        specialization = self.get_object()
        doctors = DoctorName.objects.filter(main_specialization=specialization)
        serializer = DoctorNameSimpleSerializer(doctors, many=True, context={'request': request})
        return Response(serializer.data)


class DoctorNameNestedViewSet(viewsets.ViewSet):
    permission_classes = [IsReadOnly]

    # /doctor_types/<doctor_type_pk>/doctors/<doctor_pk>/
    def retrieve(self, request, doctor_type_pk=None, pk=None):
        try:
            doctor = DoctorName.objects.get(pk=pk, main_specialization__id=doctor_type_pk)
        except DoctorName.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DoctorNameDetailSerializer(doctor, context={'request': request})
        return Response(serializer.data)


class DoctorNameNestedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DoctorNameNestedSerializer

    def get_queryset(self):
        # Pobieramy tylko lekarzy dla konkretnej specjalizacji
        return DoctorName.objects.filter(main_specialization_id=self.kwargs['doctor_type_pk'])



# Na daną chwilę nie jest nam potrzebne, przyda się jednak w przyszłości - widok na read only
# class DataViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     Read only view.
#     """
#     queryset = DoctorType.objects.all()
#     serializer_class = DoctorTypeSerializer




