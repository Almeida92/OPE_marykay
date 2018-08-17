from django.shortcuts import render

from consultoras.models import Consultora

# Create your views here.
def cadastrar(request):
    return render(request, 'consultoras/cadastrar.html')

def lista_consultoras(request):

    lista_consultoras = Consultora.objects.all()

    return render(request, 'consultoras/lista_consultoras.html', {
        'lista_consultoras': lista_consultoras
    })
