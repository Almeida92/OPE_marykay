from django.conf.urls import include, url
from django.urls import path

import consultoras.views

urlpatterns = [
    url('cadastrar/', consultoras.views.cadastrar, name='cadastrar_consultora' ),
    url('listar/', consultoras.views.lista_consultoras, name='lsita_consultora' ),
]