from django.shortcuts import render
from django.shortcuts import redirect

from principal.views import index

from produtos.models import Produto
from consultoras.models import Consultora
from .models import Estoque
# Create your views here.
def adicionar_estoque(request, cod_produto, usuario, quantidade):
  consultora = Consultora.objects.get(usuario = usuario)
  produto = Produto.objects.get(codigo = cod_produto)

  try:
    estoque_atual = Estoque.objects.get(consultora = consultora, produto = produto)  
  except:
    estoque_atual = 0
  
  if(estoque_atual):
    estoque_atual.quantidade += int(quantidade)
  else:
    estoque_atual = Estoque(
      consultora = consultora,
      produto = produto,
      quantidade = quantidade
    )

  estoque_atual.save()
  return redirect(index)

