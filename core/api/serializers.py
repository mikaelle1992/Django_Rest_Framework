from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
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
    #comentarios = ComentarioSerializer(many=True)
    #avaliacoes = AvaliacaoSerializer(many=True)
    descricao_completa = SerializerMethodField()
    class Meta:
        
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao','aprovado', 'foto',
                  'atracoes', 'comentarios','avaliacoes', 'enderecos',
                  'descricao_completa', 'descricao_completa2' )
        
        
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)