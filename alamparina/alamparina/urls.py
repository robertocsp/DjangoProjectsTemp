from django.conf.urls import patterns, include, url
from django.contrib import admin
from alamparina.views import usuario_marca
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alamparina.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # ...
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usuariomarca/$', usuario_marca),
    # ...
)
