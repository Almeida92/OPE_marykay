from django.shortcuts import render
from django.http import HttpResponse
from .form import ConsultoraForm
from .models import Consultora
from django.contrib.auth.models import User
from django.shortcuts import redirect
from consultoras.models import Consultora

def cadastrar(request):
    if request.method == 'POST':
        form = ConsultoraForm(request.POST)
        if form.is_valid():
            return criar_usuario(form, request)
    else:
        form = ConsultoraForm()
    return render(request, 'consultoras/cadastrar.html', {'form': form})
    
def criar_usuario(form, request):
    novo_usuario = User(
        username = form.cleaned_data['usuario'],
        first_name = form.cleaned_data['primeiro_nome'],
        last_name = form.cleaned_data['ultimo_nome'],
        email = form.cleaned_data['email'],
        password = form.cleaned_data['senha'],
        is_active = True)

    novo_usuario.save()
    return criar_consultora(form, novo_usuario, request)

def criar_consultora(form, usuario, request):
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
    request.session['nova_consultora'] = 1
    return redirect(lista_consultoras)

def lista_consultoras(request):
    if request.session.get('nova_consultora') == 1:
        nova_consultora = 1
        request.session['nova_consultora'] = 0
    else:
        nova_consultora = 0

    lista_consultoras = Consultora.objects.all()

    return render(request, 'consultoras/lista_consultoras.html', {
        'lista_consultoras': lista_consultoras,
        'nova_consultora': nova_consultora,
    })