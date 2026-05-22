from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Personaje
from .serializers import PersonajeSerializer
from .filters import PersonajeFilter


class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all().order_by('id')
    serializer_class = PersonajeSerializer

    parser_classes = [MultiPartParser, FormParser, JSONParser]

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]

    filterset_class = PersonajeFilter

    ordering_fields = [
        'nombre_personaje',
        'nivel_poder',
        'fecha_creacion',
        'edad',
    ]

    search_fields = [
        'nombre_personaje',
        'descripcion',
        'tipo',
        'clase_heroe',
        'rango_heroe',
        'nivel_amenaza',
        'afiliacion',
    ]