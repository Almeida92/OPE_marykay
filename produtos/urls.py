from django.conf.urls import include, url
from django.urls import path

import produtos.views

urlpatterns = [
    url('lista/', produtos.views.listar_produtos, name='lista_produtos' ),
]