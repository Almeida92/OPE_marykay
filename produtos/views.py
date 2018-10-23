from django.shortcuts import render

def listar_produtos(request):
    return render(request, 'produtos/listar.html')

