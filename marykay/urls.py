from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import principal.views

urlpatterns = [
    url(r'^$', principal.views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', principal.views.logout_view, name="logout_view"),
    url(r'^cliente/', include('cliente.urls')),
]
