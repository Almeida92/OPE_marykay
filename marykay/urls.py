from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import principal.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', principal.views.index, name='index'),
    url('login/', principal.views.login, name='login'),
    path('admin/', admin.site.urls),
]
