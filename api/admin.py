from django.contrib import admin
from .models import Personaje


@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_personaje',
        'tipo',
        'clase_heroe',
        'rango_heroe',
        'nivel_amenaza',
        'afiliacion',
        'nivel_poder',
        'fecha_creacion',
    )

    search_fields = (
        'nombre_personaje',
        'tipo',
        'clase_heroe',
        'rango_heroe',
        'nivel_amenaza',
        'afiliacion',
    )

    list_filter = (
        'tipo',
        'clase_heroe',
        'rango_heroe',
        'nivel_amenaza',
    )
