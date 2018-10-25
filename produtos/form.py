from django import forms

from .models import Categoria

class ProdutoForm(forms.Form):
    codigo = forms.CharField(
        label='Código do Produto',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))

    nome = forms.CharField(
        label='Nome do Produto',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))

    preco = forms.CharField(
        label='Preço',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    
    descricao = forms.CharField(
        label='Descrição',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))

    categorias = []

    for categoria in Categoria.objects.all():
      categorias.append((categoria.codigo, categoria.descricao))

    categoria = forms.ChoiceField(
        required=False,
        choices=categorias,
         widget=forms.Select(attrs={'class' : 'form-control'})
    )