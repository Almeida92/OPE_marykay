from django.shortcuts import render

# Create your views here.
def cadastrar(request):
    return render(request, 'consultoras/cadastrar.html')
