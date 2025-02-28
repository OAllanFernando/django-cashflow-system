from django.urls import path
from.views import CidadeCreate, CidadeUpdate , CidadeList, CidadeDelete
from.views import EstadoCreate, EstadoUpdate, EstadoList, EstadoDelete
from.views import PessoaCreate, PessoaUpdate, PessoaList, PessoaDelete
from.views import EnderecoCreate, EnderecoUpdate, EnderecoList, EnderecoDelete
from.views import ProdutoCreate, ProdutoUpdate, ProdutoList, ProdutoDelete
from.views import EntradaCreate, EntradaUpdate, EntradaList, EntradaDelete
from.views import SaidaCreate, SaidaUpdate, SaidaList, SaidaDelete
from.views import ServicoCreate, ServicoUpdate, ServicoList, ServicoDelete
from .views import ItemProdutoCreate, ItemServicoCreate #, ItemProdutoUpdate, ItemProdutoList, ItemProdutoDelete

urlpatterns = [
    path('cadastrar/estado/', EstadoCreate.as_view(), name='cadastrar-estado'),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name='editar-estado'),
    path('listar/estado/', EstadoList.as_view(), name='listar-estado'),
    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name='excluir-estado'),

    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('listar/cidade/', CidadeList.as_view(), name='listar-cidade'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),

    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='cadastrar-pessoa'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
    path('listar/pessoa/', PessoaList.as_view(), name='listar-pessoa'),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name='excluir-pessoa'),
    

    # Endereço
    path('cadastrar/endereco/', EnderecoCreate.as_view(), name='cadastrar-endereco'),
    path('editar/endereco/<int:pk>/', EnderecoUpdate.as_view(), name='editar-endereco'),
    path('listar/endereco/', EnderecoList.as_view(), name='listar-endereco'),
    path('excluir/endereco/<int:pk>/', EnderecoDelete.as_view(), name='excluir-endereco'),

    path('cadastrar/produto/', ProdutoCreate.as_view(), name='cadastrar-produto'),
    path('editar/produto/<int:pk>/', ProdutoUpdate.as_view(), name='editar-produto'),
    path('listar/produto/', ProdutoList.as_view(), name='listar-produto'),
    path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name='excluir-produto'),

    path('cadastrar/entrada/', EntradaCreate.as_view(), name='cadastrar-entrada'),
    path('editar/entrada/<int:pk>/', EntradaUpdate.as_view(), name='editar-entrada'),
    path('listar/entrada/', EntradaList.as_view(), name='listar-entrada'),
    path('excluir/entrada/<int:pk>/', EntradaDelete.as_view(), name='excluir-entrada'),

    path('cadastrar/saida/', SaidaCreate.as_view(), name='cadastrar-saida'),
    path('editar/saida/<int:pk>/', SaidaUpdate.as_view(), name='editar-saida'),
    path('listar/saida/', SaidaList.as_view(), name='listar-saida'),
    path('excluir/saida/<int:pk>/', SaidaDelete.as_view(), name='excluir-saida'),


    path('cadastrar/servico/', ServicoCreate.as_view(), name='cadastrar-servico'),
    path('editar/servico/<int:pk>/', ServicoUpdate.as_view(), name='editar-servico'),
    path('listar/servico/', ServicoList.as_view(), name='listar-servico'),
    path('excluir/servico/<int:pk>/', ServicoDelete.as_view(), name='excluir-servico'),


    path('cadastrar/item-produto/', ItemProdutoCreate.as_view(), name='cadastrar-itemproduto'),
    path('cadastrar/item-servico/', ItemServicoCreate.as_view(), name='cadastrar-itemservico'),
        
]

