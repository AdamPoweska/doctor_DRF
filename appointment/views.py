# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *
from .models import *


class DataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = DoctorType.objects.all()
    serializer_class = DoctorTypeSerializer


class DataCrudViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = DoctorType.objects.all()
    serializer_class = DoctorTypeSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # poniższy kod nadpisuje domyślny sposób zapisywania nowych obiektów, Zapisuje nowy obiekt Snippet, ale dodatkowo automatycznie ustawia pole owner na aktualnie zalogowanego użytkownika (self.request.user). Oznacza to, że użytkownik tworzący snippet automatycznie staje się jego właścicielem.
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)






