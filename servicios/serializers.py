from rest_framework import serializers

from .models import usuarios,partidas

class usuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuarios
        fields = ('id', 'password')

class partidasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = partidas
        fields = ('id', 'fecha','id_usuarios', 'minutos_jugados','puntaje')

