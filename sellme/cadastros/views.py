# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Estado, Cidade, Endereco, Pessoa, Produto, Servico, Entrada, Saida, ItemProduto, ItemServico
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView
from .filters import CidadeFilter, ProdutoFilter



class EstadoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Estado
    fields = ['nome', 'sigla', 'pais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    success_message = 'Estado cadastrado com sucesso!'

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

class CidadeList(LoginRequiredMixin, FilterView):
    template_name = 'cadastros/list/cidade.html'
    model = Cidade
    filterset_class = CidadeFilter

    def get_queryset(self):
        return Cidade.objects.all().select_related('estado')


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
        query = Pessoa.objects.filter(cadastrado_por=self.request.user).select_related('cidade')
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

    def get_queryset(self):
        return Endereco.objects.filter(cadastrado_por=self.request.user).select_related('cidade', 'pessoa')

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

class ProdutoList(LoginRequiredMixin, FilterView):
    template_name = 'cadastros/list/produto.html'
    model = Produto
    filterset_class = ProdutoFilter

    def get_queryset(self):
        return Produto.objects.filter(cadastrado_por=self.request.user)

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

    def get_queryset(self):
        return Servico.objects.filter(cadastrado_por=self.request.user)

class ServicoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-servico')
    model = Servico
    group_required = "Administrador"


###############################################################################

class EntradaCreate(LoginRequiredMixin, CreateView):
    model = Entrada
    fields = ['descricao', 'data', 'cliente']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        entrada = Entrada.objects.get(cadastrado_por=self.request.user, aberta=True)
        if entrada:
            form.add_error("aberta", 'Já existe uma entrada aberta')
            return self.form_invalid(form)
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
    
    def get_queryset(self):
        return Entrada.objects.filter(cadastrado_por=self.request.user).select_related('cliente')

class EntradaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-entrada')
    model = Entrada
    group_required = "Administrador"



###############################################################################

class SaidaCreate(LoginRequiredMixin, CreateView):
    model = Saida
    fields = ['descricao', 'data', 'cliente']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    # se já existe uma saída já redireciona para o updateView sem carregar o form
    def dispatch(self, request, *args, **kwargs):
        saida = Saida.objects.filter(cadastrado_por=self.request.user, aberta=True)
        if saida.exists():
            
            from django.http import HttpResponseRedirect
            redirect_url = reverse_lazy('editar-saida', kwargs={"pk": saida[0].pk})
            print(redirect_url)
            return HttpResponseRedirect(redirect_url)
            
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        saida = Saida.objects.filter(cadastrado_por=self.request.user, aberta=True)
        if saida.exists():
            form.add_error("aberta", 'Já existe uma saída aberta')
            return self.form_invalid(form)
        form.instance.cadastrado_por = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Saída'
        return context

class SaidaUpdate(LoginRequiredMixin, UpdateView):
    model = Saida
    fields = ['descricao', 'data', 'cliente', 'fechar_saida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        saida = Saida.objects.get(
            pk=self.kwargs["pk"], 
            # Além do id, faz um WHERE também com o usuário
            cadastrado_por=self.request.user,
            aberta=True
        )
        return saida
    
    def form_valid(self, form):

        if form.instance.fechar_saida:

            itens_produto = ItemProduto.objects.filter(usuario=self.request.user, saida__aberta=True)
            itens_servico = ItemServico.objects.filter(usuario=self.request.user, saida__aberta=True)

            if not itens_produto.exists() and not itens_servico.exists():
                form.add_error(None, 'Adicione itens a saída')
                return self.form_invalid(form)

            
            form.instance.aberta = False

        url_sucesso = super().form_valid(form)
        return url_sucesso    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Saída'
        return context


class SaidaList(LoginRequiredMixin, ListView):
    template_name = 'cadastros/list/saida.html'
    model = Saida

    def get_queryset(self):
        return Saida.objects.filter(cadastrado_por=self.request.user).select_related('cliente')

class SaidaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-saida')
    model = Saida
    group_required = "Administrador"


###############################################################################


class ItemProdutoCreate(LoginRequiredMixin, CreateView):
    model = ItemProduto
    fields = ['quantidade', 'produto', 'entrada', 'saida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['entrada'].queryset = Entrada.objects.filter(cadastrado_por=self.request.user, aberta=True)
        form.fields['saida'].queryset = Saida.objects.filter(cadastrado_por=self.request.user, aberta=True)
        return form

    def form_valid(self, form):
        if form.instance.entrada and form.instance.saida:
            form.add_error("entrada", 'Item não pode estar em uma entrada e saída ao mesmo tempo')
            form.add_error("saida", 'Item não pode estar em uma entrada e saída ao mesmo tempo')
            return self.form_invalid(form)
        
        if not form.instance.entrada and not form.instance.saida:
            form.add_error("entrada", 'Item deve estar em uma entrada ou saída')
            form.add_error("saida", 'Item deve estar em uma entrada ou saída')
            return self.form_invalid(form)
        
        form.instance.usuario = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar de Item de Produto'
        return context
    
class ItemServicoCreate(LoginRequiredMixin, CreateView):
    model = ItemServico
    fields = ['quantidade', 'servico', 'entrada', 'saida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['entrada'].queryset = Entrada.objects.filter(cadastrado_por=self.request.user, aberta=True)
        form.fields['saida'].queryset = Saida.objects.filter(cadastrado_por=self.request.user, aberta=True)
        return form

    def form_valid(self, form):
        if form.instance.entrada and form.instance.saida:
            form.add_error("entrada", 'Item não pode estar em uma entrada e saída ao mesmo tempo')
            form.add_error("saida", 'Item não pode estar em uma entrada e saída ao mesmo tempo')
            return self.form_invalid(form)
        
        if not form.instance.entrada and not form.instance.saida:
            form.add_error("entrada", 'Item deve estar em uma entrada ou saída')
            form.add_error("saida", 'Item deve estar em uma entrada ou saída')
            return self.form_invalid(form)
        
        form.instance.usuario = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar de Item de Serviço'
        return context
