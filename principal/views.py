from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

from estoque.models import Estoque
from consultoras.models import Consultora

# Create your views here.
@login_required
def index(request):
  qtd_estoque = consultar_estoque(request.user)

  return render(request, 'principal/index.html', {
    'estoque': qtd_estoque
  })

def consultar_estoque(usuario):
  consultora = Consultora.objects.get(usuario = usuario.id)
  estoque = Estoque.objects.filter(consultora = consultora.id)
  total = 0

  for produto in estoque:
    total += produto.quantidade

  return total

def logout_view(request):
  logout(request)
  return redirect('/')
