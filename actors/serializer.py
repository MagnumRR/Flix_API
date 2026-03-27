# Importando do módulo "rest_framework" o módulo "serializer"
from rest_framework import serializers
# Importando do projeto "actors" o Model "Actor"
from actors.models import Actor


# Classe Serializer para ator:
class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'
