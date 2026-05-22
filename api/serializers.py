from rest_framework import serializers
from .models import Personaje


class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'

    def validate(self, data):
        tipo = data.get('tipo', getattr(self.instance, 'tipo', None))
        clase_heroe = data.get('clase_heroe', getattr(self.instance, 'clase_heroe', None))
        rango_heroe = data.get('rango_heroe', getattr(self.instance, 'rango_heroe', None))
        nivel_amenaza = data.get('nivel_amenaza', getattr(self.instance, 'nivel_amenaza', None))

        if tipo == 'Heroe':
            if not clase_heroe:
                raise serializers.ValidationError({
                    'clase_heroe': 'Si el personaje es héroe, debe indicar la clase del héroe.'
                })

            if not rango_heroe:
                raise serializers.ValidationError({
                    'rango_heroe': 'Si el personaje es héroe, debe indicar el rango del héroe.'
                })

            if nivel_amenaza:
                raise serializers.ValidationError({
                    'nivel_amenaza': 'Un héroe no debe tener nivel de amenaza.'
                })

        elif tipo == 'Kaijin':
            if not nivel_amenaza:
                raise serializers.ValidationError({
                    'nivel_amenaza': 'Si el personaje es kaijin, debe indicar el nivel de amenaza.'
                })

            if clase_heroe or rango_heroe:
                raise serializers.ValidationError({
                    'tipo': 'Un kaijin no debe tener clase ni rango de héroe.'
                })

        elif tipo == 'Civil':
            if clase_heroe or rango_heroe or nivel_amenaza:
                raise serializers.ValidationError({
                    'tipo': 'Un civil no debe tener clase, rango ni nivel de amenaza.'
                })

        return data