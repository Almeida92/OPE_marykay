from django.db import models

class Categoria(models.Model):
  codigo = models.IntegerField(default= 0 )
  descricao = models.CharField(max_length=100, default= '')  

class Produto(models.Model):
  codigo = models.CharField(max_length=100, default= '')
  nome = models.CharField(max_length=100, default= '')
  preco = models.DecimalField(max_digits=6, decimal_places=2)
  descricao = models.CharField(max_length=100, default= '')
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria")
  