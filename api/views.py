from rest_framework import viewsets
from rest_framework import pagination
from api.models import DadosPerfil
from api.serializers import DadosPerfilSerializer


# class DadosPerfilPagination(pagination.PageNumberPagination):
#     page_size: 1
#     page_size_query_param = 'page_size'
#     max_page_size = 50

class DadosPerfilViewSet(viewsets.ModelViewSet):
    serializer_class = DadosPerfilSerializer
    queryset = DadosPerfil.objects.all()
    # pagination_class = DadosPerfilPagination