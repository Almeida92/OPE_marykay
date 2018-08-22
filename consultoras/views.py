from django.shortcuts import render
from django.http import HttpResponse
from .form import ConsultoraForm

from consultoras.models import Consultora

def cadastrar(request):
    if request.method == 'POST':
        form = ConsultoraForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['primeiro_nome'])
    else:
        form = ConsultoraForm()
    return render(request, 'consultoras/cadastrar.html', {'form': form})
    
def lista_consultoras(request):

    lista_consultoras = Consultora.objects.all()

    return render(request, 'consultoras/lista_consultoras.html', {
        'lista_consultoras': lista_consultoras
    })
