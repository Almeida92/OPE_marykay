from django.db import models
from django.contrib.auth.models import User

class Consultora(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
  nivel = models.CharField(max_length=200)
  sexo = models.CharField(max_length=1)
  status = models.CharField(max_length=200)
  cpf = models.CharField(max_length=200)
  data_nascimento = models.DateTimeField('Data de nascimento')

