from django.shortcuts import render
from .form import ProdutoForm

def listar_produtos(request):
    return render(request, 'produtos/listar.html')

def cadastrar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            return true
            # return criar_produto(form, request)
    else:
        form = ProdutoForm()

    return render(request, 'produtos/cadastrar.html', {'form': form})