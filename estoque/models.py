from django.db import models

from produtos.models import Produto
from consultoras.models import Consultora

# Create your models here.
class Estoque(models.Model):
  consultora = models.ForeignKey(Consultora, on_delete=models.CASCADE, related_name="consultora")
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="produto")
  quantidade = models.IntegerField(default= 0)
  