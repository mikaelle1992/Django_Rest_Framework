from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoSerializer(ModelSerializer):
    # criar um serializer simples, leve
    class Meta:
        model = Avaliacao
        fields = ['id', 'user', 'comentario', 'nota', 'data']


