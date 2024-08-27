# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Estado, Cidade, Endereco, Pessoa, Produto, Servico, Entrada, Saida
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy


class EstadoCreate(LoginRequiredMixin, CreateView):
    model = Estado
    fields = ['nome', 'sigla', 'pais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Estado'
        return context


class EstadoUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Estado'
        return context

class EstadoList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/estado.html'
    model = Estado
    
    def get_queryset(self):
        return Estado.objects.all()

class EstadoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estado')
    model = Estado

###############################################################################


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Cidade'
        return context


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Cidade'
        return context
    

class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    group_required = "Administrador"

class CidadeList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/cidade.html'
    model = Cidade


###############################################################################

class PessoaCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    fields = ['nome', 'sobrenome', 'cpf', 'email', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    filds = ['nome', 'sobrenome', 'cpf', 'email', 'telefone']

    def form_valid(self, form):
        # Antes de criar objeto e salvar no banco
        form.instance.cadastrado_por = self.request.user
        url_sucesso = super().form_valid(form)
        # Depois de criar objeto e salvar no banco
        # self.object.nome_completo = self.object.nome_completo + "@"
        # from hashlib import md5
        # self.object.codigo = md5(self.object.pk)
        # self.object.save()
        return url_sucesso

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de cliente/fornecedor'
        return context

class PessoaUpdate(LoginRequiredMixin, UpdateView):
    model = Pessoa
    fields = ['nome', 'sobrenome', 'cpf', 'email', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

     # Alterar a consulta padrão que retorna o objeto com base no id
    def get_object(self):
        pessoa = Pessoa.objects.get(
            pk=self.kwargs["pk"], 
            # Além do id, faz um WHERE também com o usuário
            cadastrado_por=self.request.user 
        )
        return pessoa


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de cliente/fornecedor'
        return context
    
class PessoaList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/pessoa.html'
    model = Pessoa
    
     # Altera a query padrão para consuultar registros (SELECT)
    def get_queryset(self):
        query = Pessoa.objects.filter(cadastrado_por=self.request.user)
        return query

class PessoaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    group_required = "Administrador"


###############################################################################

class EnderecoCreate(LoginRequiredMixin, CreateView):
    model = Endereco
    fields = ['rua', 'numero', 'bairro', 'cidade', 'pessoa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Endereço'
        return context

class EnderecoUpdate(LoginRequiredMixin, UpdateView):
    model = Endereco
    fields = ['rua', 'numero', 'bairro', 'cidade', 'pessoa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Endereço'
        return context
    
class EnderecoList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/endereco.html'
    model = Endereco

class EnderecoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-endereco')
    model = Endereco
    group_required = "Administrador"



###############################################################################

class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'urlImagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Produto'
        return context

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'urlImagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        produto = Produto.objects.get(
            pk=self.kwargs["pk"], 
            cadastrado_por=self.request.user 
        )
        return produto


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Produto'
        return

class ProdutoList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/produto.html'
    model = Produto

class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto')
    model = Produto
    group_required = "Administrador"

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
    model = Servico
    fields = ['nome', 'descricao', 'preco', 'urlImagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Serviço'
        return context
    
class ServicoUpdate(LoginRequiredMixin, UpdateView):
    model = Servico
    fields = ['nome', 'descricao', 'preco', 'urlImagem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        servico = Servico.objects.get(
            pk=self.kwargs["pk"], 
            # Além do id, faz um WHERE também com o usuário
            cadastrado_por=self.request.user 
        )
        return servico


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Serviço'
        return

class ServicoList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/servico.html'
    model = Servico

class ServicoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-servico')
    model = Servico
    group_required = "Administrador"


###############################################################################

class EntradaCreate(LoginRequiredMixin, CreateView):
    model = Entrada
    fields = ['descricao', 'data', 'valor', 'itens', 'cliente', 'servico']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Entrada'
        return context

class EntradaUpdate(LoginRequiredMixin, UpdateView):
    model = Entrada
    fields = ['descricao', 'data', 'valor', 'itens', 'cliente', 'servico']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        entrada = Entrada.objects.get(
            pk=self.kwargs["pk"], 
            # Além do id, faz um WHERE também com o usuário
            cadastrado_por=self.request.user 
        )
        return entrada

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Entrada'
        return context

class EntradaList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/entrada.html'
    model = Entrada

class EntradaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-entrada')
    model = Entrada
    group_required = "Administrador"



###############################################################################

class SaidaCreate(LoginRequiredMixin, CreateView):
    model = Saida
    fields = ['descricao', 'data', 'valor', 'itens', 'cliente']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Saída'
        return context

class SaidaUpdate(LoginRequiredMixin, UpdateView):
    model = Saida
    fields = ['descricao', 'data', 'valor', 'itens', 'cliente']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        entrada = Entrada.objects.get(
            pk=self.kwargs["pk"], 
            # Além do id, faz um WHERE também com o usuário
            cadastrado_por=self.request.user 
        )
        return entrada

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Saída'
        return context

class SaidaList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/saida.html'
    model = Saida

class SaidaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-saida')
    model = Saida
    group_required = "Administrador"


###############################################################################

