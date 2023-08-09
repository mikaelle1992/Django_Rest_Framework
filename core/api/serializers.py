from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    # criar um serializer simples, leve
    
    #aninhamento de outro objetos que vem de outra classe
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecoSerializer()
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    class Meta:
        
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao','aprovado', 'foto',
                  'atracoes', 'comentarios','avaliacoes', 'enderecos' )