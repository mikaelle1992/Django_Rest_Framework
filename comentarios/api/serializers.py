from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario


class ComentarioSerializer(ModelSerializer):
    # criar um serializer simples, leve
    class Meta:
        model = Comentario
        fields = ('id', 'usuario', 'comentario', 'data', 'aprovado')



