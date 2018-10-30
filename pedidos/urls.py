from django.conf.urls import include, url
from django.urls import path

from .views import importar_pedidos

urlpatterns = [
    url('importar/', importar_pedidos , name='importar_pedidos' ),
]