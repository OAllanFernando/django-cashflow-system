from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.sigla} - {self.pais}"
        # return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome}"
        # return self.nome
    

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='enderecos')
    
    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.bairro}"


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    urlImagem = models.URLField(max_length=200)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome}"
        # return self.nome

# fazer item entrada e saida diferentes (classes) 
class Item(models.Model):
    quantidade = models.IntegerField()
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.quantidade} - {self.produto.nome}"
    
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    urlImagem = models.URLField(max_length=200)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome}"
        # return self.nome


# 
class Entrada(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    itens = models.ManyToManyField(Item, related_name='item_entradas')
    cliente = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    servico = models.ManyToManyField(Servico, related_name='entradas')
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"Entrada: {self.descricao} - {self.data}"

# Pensei aqui e podemos adicionar servicos em saids, no caso, o cliente pode ter comprado um produto e um servico
class Saida(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    itens = models.ManyToManyField(Item, related_name='item_saidas')
    cliente = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"Saída: {self.descricao} - {self.data}"