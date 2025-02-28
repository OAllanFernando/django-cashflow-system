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
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    # itens = models.ManyToManyField(Item, related_name='item_entradas')
    cliente = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    # servico = models.ManyToManyField(Servico, related_name='entradas')
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    aberta = models.BooleanField(default=True)

    def __str__(self):
        return f"Entrada: {self.descricao} - {self.data}"

# Pensei aqui e podemos adicionar servicos em saids, no caso, o cliente pode ter comprado um produto e um servico
class Saida(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    # itens = models.ManyToManyField(Item, related_name='item_saidas')
    cliente = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    aberta = models.BooleanField(default=True)
    fechar_saida = models.BooleanField(default=False, verbose_name='Fechar saída')

    def __str__(self):
        return f"Saída: {self.descricao} - {self.data}"
    

    # fazer item entrada e saida diferentes (classes)   
class ItemProduto(models.Model):
    quantidade = models.IntegerField()
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    entrada = models.ForeignKey(Entrada, on_delete=models.PROTECT, related_name='itens_entrada', null=True, blank=True)
    saida = models.ForeignKey(Saida, on_delete=models.PROTECT, related_name='itens_saida', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)


    def save(self, *args, **kwargs):
        if self.entrada and self.saida:
            raise ValueError("Item não pode estar em uma entrada e saída ao mesmo tempo")
        
        if not self.entrada and not self.saida:
            raise ValueError("Item deve estar em uma entrada ou saída")
        
        super(ItemProduto, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.quantidade} - {self.produto.nome}"
    

class ItemServico(models.Model):
    quantidade = models.IntegerField()
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    entrada = models.ForeignKey(Entrada, on_delete=models.PROTECT, related_name='itens_servico_entrada', null=True)
    saida = models.ForeignKey(Saida, on_delete=models.PROTECT, related_name='itens_servico_saida', null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if self.entrada and self.saida:
            raise ValueError("Item não pode estar em uma entrada e saída ao mesmo tempo")
        if not self.entrada and not self.saida:
            raise ValueError("Item deve estar em uma entrada ou saída")
        super(ItemServico, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantidade} - {self.servico.nome}"

