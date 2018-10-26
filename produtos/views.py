from django.shortcuts import render
from .form import ProdutoForm
from django.shortcuts import redirect

from .models import Produto, Categoria

def listar_produtos(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {
        'lista_produtos': lista_produtos
    })

def cadastrar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            return criar_produto(form, request)
    else:
        form = ProdutoForm()

    return render(request, 'produtos/cadastrar.html', {'form': form})

def criar_produto(form, request):
    categoria = Categoria.objects.get(codigo=form.cleaned_data['categoria'])

    novo_produto = Produto(
        codigo = form.cleaned_data['codigo'],
        nome = form.cleaned_data['nome'],
        preco = form.cleaned_data['preco'],
        descricao = form.cleaned_data['descricao'],
        categoria = categoria)

    novo_produto.save()
    return redirect(listar_produtos)