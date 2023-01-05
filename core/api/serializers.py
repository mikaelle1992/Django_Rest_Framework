from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    # criar um serializer simples, leve
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao')