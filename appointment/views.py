# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *
from .models import *


class AppointmentDateCrudViewSet(viewsets.ModelViewSet):
    """
    (C)reate (R)ead (U)date (D)elete actions.
    """
    queryset = AppointmentDates.objects.all()
    serializer_class = AppointmentDatesSerializer


class DoctorNameCrudViewSet(viewsets.ModelViewSet):
    """
    (C)reate (R)ead (U)date (D)elete actions.
    """
    queryset = DoctorName.objects.all()
    serializer_class = DoctorNameSerializer


class DoctorTypeCrudViewSet(viewsets.ModelViewSet):
    """
    (C)reate (R)ead (U)date (D)elete actions.
    """
    queryset = DoctorType.objects.all()
    serializer_class = DoctorTypeSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # z tutoriala, do użycia przy logowaniu użytkowników

    # poniższy kod (z tutoriala) nadpisuje domyślny sposób zapisywania nowych obiektów, Zapisuje nowy obiekt Snippet, ale dodatkowo automatycznie ustawia pole owner na aktualnie zalogowanego użytkownika (self.request.user). Oznacza to, że użytkownik tworzący snippet automatycznie staje się jego właścicielem.
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)






# Na daną chwilę nie jest nam potrzebne, przyda się jednak w przyszłości - widok na read only
# class DataViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     Read only view.
#     """
#     queryset = DoctorType.objects.all()
#     serializer_class = DoctorTypeSerializer




