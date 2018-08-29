from django import forms

class ConsultoraForm(forms.Form):

    primeiro_nome = forms.CharField(
        label='Primeiro Nome',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    ultimo_nome = forms.CharField(
        label='Último Nome',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    cpf = forms.CharField(
        label='CPF',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    sexo = forms.ChoiceField(choices=[('f','(F)'), ('m','(M)')], widget=forms.RadioSelect())
    endereco = forms.CharField(
        label='Endereço',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    bairro = forms.CharField(
        label='Bairro',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    cidade = forms.CharField(
        label='Cidade',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    dt_nascimento = forms.DateField(label= 'Data de Nascimento', widget=forms.TextInput(
        attrs={'class' : 'form-control', 'type': 'date'}))
    telefone = forms.CharField(
        label='Telefone',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    celular = forms.CharField(
        label='Celular',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    status = forms.CharField(
        label='status',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    nivel = forms.CharField(
        label='nivel',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    desconto = forms.CharField(
        label='Desconto',
        max_length=100,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))
    