from django.shortcuts import render

# Create your views here.

def cadastro_cliente(request):
    
    return render(request, 'cliente/cadastro-cliente.html')