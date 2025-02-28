from django.contrib import admin

# Register your models here.

from .models import Pessoa, Estado, Cidade, Endereco, Produto, ItemProduto, ItemServico, Entrada, Saida, Servico


admin.site.register(Pessoa)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Endereco)
admin.site.register(Produto)
admin.site.register(ItemProduto)
admin.site.register(ItemServico)
admin.site.register(Entrada)
admin.site.register(Saida)
admin.site.register(Servico)


