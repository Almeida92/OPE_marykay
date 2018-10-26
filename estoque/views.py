from django.shortcuts import render
from django.shortcuts import redirect

from principal.views import index

from produtos.models import Produto
from consultoras.models import Consultora
from .models import Estoque
# Create your views here.
def adicionar_estoque(request, cod_produto, usuario, quantidade):
  produto = Produto.objects.get(codigo = cod_produto)
  consultora = Consultora.objects.get(usuario = usuario)
  
  estoque = Estoque(
    consultora = consultora,
    produto = produto,
    quantidade = quantidade
  )

  estoque.save()
  return redirect(index)

