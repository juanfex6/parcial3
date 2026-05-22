from django.db import models
from django.core.exceptions import ValidationError


class Personaje(models.Model):
    TIPO_CHOICES = [
        ('Heroe', 'Héroe'),
        ('Kaijin', 'Kaijin'),
        ('Civil', 'Civil'),
    ]

    CLASE_HEROE_CHOICES = [
        ('Clase S', 'Clase S'),
        ('Clase A', 'Clase A'),
        ('Clase B', 'Clase B'),
        ('Clase C', 'Clase C'),
        ('Sin clase', 'Sin clase'),
    ]

    RANGO_HEROE_CHOICES = [
        ('Rango 1', 'Rango 1'),
        ('Rango 2', 'Rango 2'),
        ('Rango 3', 'Rango 3'),
        ('Rango 4', 'Rango 4'),
        ('Rango 5', 'Rango 5'),
        ('Sin rango', 'Sin rango'),
    ]

    NIVEL_AMENAZA_CHOICES = [
        ('Lobo', 'Lobo'),
        ('Tigre', 'Tigre'),
        ('Demonio', 'Demonio'),
        ('Dragón', 'Dragón'),
        ('Dios', 'Dios'),
    ]

    nombre_personaje = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='personajes/', null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    # Tipo general del personaje
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    # Solo para héroes
    clase_heroe = models.CharField(
        max_length=20,
        choices=CLASE_HEROE_CHOICES,
        null=True,
        blank=True
    )

    rango_heroe = models.CharField(
        max_length=20,
        choices=RANGO_HEROE_CHOICES,
        null=True,
        blank=True
    )

    # Solo para kaijin
    nivel_amenaza = models.CharField(
        max_length=20,
        choices=NIVEL_AMENAZA_CHOICES,
        null=True,
        blank=True
    )

    # Atributos generales
    afiliacion = models.CharField(max_length=100, null=True, blank=True)
    nivel_poder = models.IntegerField()
    edad = models.IntegerField(null=True, blank=True)

    def clean(self):
        if self.tipo == 'Heroe':
            if not self.clase_heroe:
                raise ValidationError('Si el personaje es héroe, debe tener clase de héroe.')

            if not self.rango_heroe:
                raise ValidationError('Si el personaje es héroe, debe tener rango de héroe.')

            if self.nivel_amenaza:
                raise ValidationError('Un héroe no debe tener nivel de amenaza.')

        elif self.tipo == 'Kaijin':
            if not self.nivel_amenaza:
                raise ValidationError('Si el personaje es kaijin, debe tener nivel de amenaza.')

            if self.clase_heroe or self.rango_heroe:
                raise ValidationError('Un kaijin no debe tener clase ni rango de héroe.')

        elif self.tipo == 'Civil':
            if self.clase_heroe or self.rango_heroe or self.nivel_amenaza:
                raise ValidationError('Un civil no debe tener clase, rango ni nivel de amenaza.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_personaje
