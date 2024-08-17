# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import Estado, Cidade, Endereco, Pessoa, Produto, Servico, Entrada, Saida
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy


class EstadoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Estado
    fields = ['nome', 'sigla', 'pais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Estado'
        return context


class EstadoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Estado'
        return context

class EstadoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/list/estado.html'
    model = Estado

class EstadoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estado')
    model = Estado

###############################################################################


class CidadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Cidade'
        return context


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Cidade'
        return context
    

class CidadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade


class CidadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/list/cidade.html'
    model = Cidade


###############################################################################

class PessoaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pessoa
    fields = ['nome', 'sobrenome', 'cpf', 'email', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de cliente/fornecedor'
        return context

class PessoaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pessoa
    fields = ['nome', 'sobrenome', 'cpf', 'email', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de cliente/fornecedor'
        return context
    
class PessoaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/list/pessoa.html'
    model = Pessoa

class PessoaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa

###############################################################################

class EnderecoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['rua', 'numero', 'bairro', 'cidade', 'pessoa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Endereço'
        return context

class EnderecoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['rua', 'numero', 'bairro', 'cidade', 'pessoa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Endereço'
        return context
    
class EnderecoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/list/endereco.html'
    model = Endereco

class EnderecoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-endereco')
    model = Endereco


###############################################################################

class ProdutoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'urlImagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Produto'
        return context

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'urlImagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Produto'
        return

class ProdutoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/list/produto.html'
    model = Produto

class ProdutoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto')
    model = Produto


###############################################################################

# class ItemCreate(CreateView):
#     model = Item
#     fields = ['quantidade', 'produto']
#     template_name = 'cadastros/form.html'
#     success_url = reverse_lazy('index')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['titulo'] = 'Cadastro de Item'
#         return context

# class ItemUpdate(UpdateView):
#     model = Item
#     fields = ['quantidade', 'produto']
#     template_name = 'cadastros/form.html'
#     success_url = reverse_lazy('index')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['titulo'] = 'Atualização de Item'
#         return

###############################################################################

class ServicoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Servico
    fields = ['nome', 'descricao', 'preco', 'urlImagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Serviço'
        return context
    
class ServicoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Servico
    fields = ['nome', 'descricao', 'preco', 'urlImagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Serviço'
        return

class ServicoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/list/servico.html'
    model = Servico

class ServicoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-servico')
    model = Servico


###############################################################################

class EntradaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Entrada
    fields = ['descricao', 'data', 'valor', 'itens', 'cliente', 'servico']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Entrada'
        return context

class EntradaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Entrada
    fields = ['descricao', 'data', 'valor', 'itens', 'cliente', 'servico']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Entrada'
        return context

class EntradaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/list/entrada.html'
    model = Entrada

class EntradaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-entrada')
    model = Entrada


###############################################################################

class SaidaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Saida
    fields = ['descricao', 'data', 'valor', 'itens', 'cliente']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Saída'
        return context

class SaidaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Saida
    fields = ['descricao', 'data', 'valor', 'itens', 'cliente']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Saída'
        return context

class SaidaList(LoginRequiredMixin, ListView): 
    login_url = reverse_lazy('login')
    template_name = 'cadastros/list/saida.html'
    model = Saida

class SaidaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-saida')
    model = Saida

###############################################################################

