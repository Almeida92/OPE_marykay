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
    sexo = forms.ChoiceField(choices=[('f','(F)'), ('m','(M)')], widget=forms.RadioSelect())
