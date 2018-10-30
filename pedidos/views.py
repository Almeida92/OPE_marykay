from django.shortcuts import render

# Create your views here.
def importar_pedidos(request):
  return render(request, 'pedidos/importar.html')
