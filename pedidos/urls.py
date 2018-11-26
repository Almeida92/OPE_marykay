from django.conf.urls import include, url
from django.urls import path

from .views import importar_pedidos, consultar_pedidos

urlpatterns = [
    url('importar/', importar_pedidos , name='importar_pedidos' ),
    url('consultar/', consultar_pedidos , name='consultar_pedidos' ),
]