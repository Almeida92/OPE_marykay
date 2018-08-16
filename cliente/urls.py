from django.conf.urls import include, url
from django.urls import path

import cliente.views

urlpatterns = [
    path('cadastrar/', cliente.views.cadastro_cliente, name="cadastro_cliente")
]
