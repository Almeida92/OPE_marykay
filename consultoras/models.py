from django.db import models
from django.contrib.auth.models import User

class Consultora(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
  primeiro_nome = models.CharField(max_length=100, default= '')
  ultimo_nome = models.CharField(max_length=100, default= '')
  cpf = models.CharField(max_length=200)
  data_nascimento = models.DateTimeField('Data de nascimento')
  sexo = models.CharField(max_length=1)
  endereco = models.CharField(max_length=100, default= '')
  bairro = models.CharField(max_length=100, default= '')
  cidade = models.CharField(max_length=100, default= '')
  telefone = models.CharField(max_length=100, default= '')
  celular = models.CharField(max_length=100, default= '')
  status = models.CharField(max_length=100, default= '')
  nivel = models.CharField(max_length=100, default= '')
  desconto = models.CharField(max_length=100, default= '')
    

