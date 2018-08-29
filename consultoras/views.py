from django.shortcuts import render
from django.http import HttpResponse
from .form import ConsultoraForm
from .models import Consultora
from django.contrib.auth.models import User

from consultoras.models import Consultora

def cadastrar(request):
    if request.method == 'POST':
        form = ConsultoraForm(request.POST)
        if form.is_valid():
            criar_consultora(form)
    else:
        form = ConsultoraForm()
    return render(request, 'consultoras/cadastrar.html', {'form': form})
    
def lista_consultoras(request):

    lista_consultoras = Consultora.objects.all()

    return render(request, 'consultoras/lista_consultoras.html', {
        'lista_consultoras': lista_consultoras
    })

def criar_consultora(form):
    usuario = User.objects.get(id=1)

    nova_consultora = Consultora(
        usuario = usuario,
        primeiro_nome = form.cleaned_data['primeiro_nome'],
        ultimo_nome = form.cleaned_data['ultimo_nome'],
        cpf = form.cleaned_data['cpf'],
        data_nascimento = form.cleaned_data['dt_nascimento'],
        sexo = form.cleaned_data['sexo'],
        endereco = form.cleaned_data['endereco'],
        bairro = form.cleaned_data['bairro'],
        cidade = form.cleaned_data['cidade'],
        telefone = form.cleaned_data['telefone'],
        celular = form.cleaned_data['celular'],
        status = form.cleaned_data['status'],
        nivel = form.cleaned_data['nivel'],
        desconto = form.cleaned_data['desconto'])
    
    nova_consultora.save()
