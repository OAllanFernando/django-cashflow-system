from django_filters import FilterSet
from .models import Cidade, Produto


class CidadeFilter(FilterSet):
    class Meta:
        model = Cidade
        fields = {
            'nome': ['icontains'],
            'estado': ['exact'],
        }

class ProdutoFilter(FilterSet):
    class Meta:
        model = Produto
        fields = {
            'nome': ['icontains'],
            'descricao': ['icontains'],
            'preco': ['exact'],
        }