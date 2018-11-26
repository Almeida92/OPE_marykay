from django.db import models
from produtos.models import Produto
from consultoras.models import Consultora
import datetime

# Create your models here.
class Pedido(models.Model):
  data_pedido = models.DateField(default=datetime.date.today, blank=True)
  consultora = models.ForeignKey(Consultora, on_delete=models.CASCADE, related_name="id_consultora")

class PedidoProduto(models.Model):
  quantidade = models.IntegerField(default= 0)
  pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="id_pedido")
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="id_produto")