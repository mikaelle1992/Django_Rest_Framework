from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
# from rest_framework.authentication import TokenAuthentication



class PontoTuristicoViewSet(ModelViewSet):

    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    #permission_classes = [IsAuthenticated]
    #authentication_classes = [TokenAuthentication]
    search_fields = ['nome', 'descricao','enderecos__linha1']

    # lookup_field = 'nome' , alterando o lookup_field padrão de enpoint 

    #filter pelo campo aprovado
    # def get_queryset(self):
    #     return PontoTuristico.objects.filter(aprovado=True)

     #filter pelos campos passados na url
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id and nome and descricao:
            queryset = PontoTuristico.objects.filter(pk=id)
            queryset = queryset.filter(nome__iexact=nome)
            queryset =queryset.filter(descricao__iexact=descricao)
        return queryset

    # def list(self, request, *args, **kwargs):
    #     return Response({'teste':123}) 

    # def create(self, request, *args, **kwargs):
    #     return Response(
    #         {'aprovado':request.data['aprovado'],
    #         'nome':request.data['nome'],
    #         'descrição':request.data['descricao'],
    #         })

    # def destroy(self, request, *args, **kwargs):
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    #     #busca um dado pelo id 
    #     pass

    # def update(self, request, *args, **kwargs):
    #     pass   

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # action personalizado, detail =True é usando porque é passando o pk 
    # @action(methods=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass

    # detail = False porque o pk não é passado 
    # @action(methods=['get'], detail=False)
    # def teste(self, request):
    #     pass