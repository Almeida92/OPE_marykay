from django.conf.urls import include, url
from django.urls import path

from .views import importar_pedidos, consultar_pedidos, pedido_detalhe

urlpatterns = [
    url('importar/', importar_pedidos , name='importar_pedidos' ),
    url('consultar/', consultar_pedidos , name='consultar_pedidos' ),
    url(r'(?P<pedido>[0-9A-Za-z._%+-]+)', pedido_detalhe , name='pedido_detalhe'), 
]