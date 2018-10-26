from django.conf.urls import include, url
from django.urls import path

from .views import adicionar_estoque

urlpatterns = [
    url('inserir/(?P<cod_produto>[-\w]+)/(?P<usuario>[-\w]+)/(?P<quantidade>[-\w]+)/', adicionar_estoque , name='adicionar_estoque' ),
]