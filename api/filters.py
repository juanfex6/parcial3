import django_filters
from .models import Personaje


class PersonajeFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(
        field_name='nombre_personaje',
        lookup_expr='icontains'
    )

    tipo = django_filters.CharFilter(
        field_name='tipo',
        lookup_expr='icontains'
    )

    clase_heroe = django_filters.CharFilter(
        field_name='clase_heroe',
        lookup_expr='icontains'
    )

    rango_heroe = django_filters.NumberFilter(
    field_name='rango_heroe'
    )

    min_rango = django_filters.NumberFilter(
    field_name='rango_heroe',
    lookup_expr='gte'
    )

    max_rango = django_filters.NumberFilter(
    field_name='rango_heroe',
    lookup_expr='lte'
    )

    nivel_amenaza = django_filters.CharFilter(
        field_name='nivel_amenaza',
        lookup_expr='icontains'
    )

    afiliacion = django_filters.CharFilter(
        field_name='afiliacion',
        lookup_expr='icontains'
    )

    min_poder = django_filters.NumberFilter(
        field_name='nivel_poder',
        lookup_expr='gte'
    )

    max_poder = django_filters.NumberFilter(
        field_name='nivel_poder',
        lookup_expr='lte'
    )

    class Meta:
        model = Personaje
        fields = [
            'nombre',
            'tipo',
            'clase_heroe',
            'rango_heroe',
            'nivel_amenaza',
            'afiliacion',
            'min_poder',
            'max_poder',
            'min_rango',
            'max_rango',
        ]