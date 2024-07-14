# from django.shortcuts import render

# Create your views here.

from .models import Estado, Cidade, Endereco, Pessoa
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


class EstadoCreate(CreateView):
    model = Estado
    fields = ['nome', 'sigla', 'pais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Estado'
        return context


class EstadoUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Estado'
        return context


###############################################################################


class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Cidade'
        return context


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de Cidade'
        return context

