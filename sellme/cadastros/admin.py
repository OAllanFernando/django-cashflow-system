from django.contrib import admin

# Register your models here.

from .models import Pessoa, Estado, Cidade, Endereco, Produto, Item, Entrada, Saida, Servico


admin.site.register(Pessoa)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Endereco)
admin.site.register(Produto)
admin.site.register(Item)
admin.site.register(Entrada)
admin.site.register(Saida)
admin.site.register(Servico)


