from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

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