from __future__ import unicode_literals

from django.db import models


# Create your models here.
class TimeStamped(models.Model):
    class Meta:
        abstract = True

    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)


class Produto(TimeStamped):
    titulo = models.CharField(max_length=100)
    sku = models.CharField(max_length=24)

    def __unicode__(self):
        return "%s" % self.titulo


class Safra(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.IntegerField()
    dtinicio = models.DateField()
    dtfim = models.DateField()

    def __unicode__(self):
        return "%s" % self.nome

class Produtos(models.Model):
    nome = models.CharField(max_length=50)
    prmedio = models.DecimalField(max_digits=55, decimal_places=2)

    def __unicode__(self):
        return "%s" % self.nome

class Servicos(models.Model):
    nome = models.CharField(max_length=50)
    dtinicio = models.DateField()
    dtfim = models.DateField()
    produto = models.ForeignKey(Produtos)
    qtdade = models.DecimalField(max_digits=15, decimal_places=2)
    valor = models.DecimalField(max_digits=15, decimal_places=2)

    def __unicode__(self):
        return "%s" % self.servico.nome


CATEGORIAS_CHOICES = (
    ("Aleatorio", "Aleatorio"),
    ("Eletronico", "Eletronico"),
    ("Eletrodomestico", "Eletrodomestico"),
)


class Balcao(TimeStamped):
    categoria = models.CharField(max_length=100, choices=CATEGORIAS_CHOICES)

    def __unicode__(self):
        return "%s" % self.categoria


class Item(TimeStamped):
    produto = models.ForeignKey(Produto)
    quantidade = models.CharField(max_length=3)
    balcao = models.ForeignKey(Balcao, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.produto.titulo
