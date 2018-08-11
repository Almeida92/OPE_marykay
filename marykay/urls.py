from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views
import consultoras.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
    url('cadastrar/', consultoras.views.cadastrar, name='cadastrarconsultora' ),
    url('lista-consultoras/', consultoras.views.lista_consultoras, name='listaconsultoras' ),
]
