from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import consultoras.views
import principal.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', principal.views.index, name='index'),
    path('admin/', admin.site.urls),
    url('cadastrar/', consultoras.views.cadastrar, name='cadastrarconsultora' ),
    url('lista-consultoras/', consultoras.views.lista_consultoras, name='listaconsultoras' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', principal.views.logout_view, name="logout_view")
]
