from django.conf.urls import patterns, include, url
from django.contrib import admin
from sitetest.views import hello, current_datetime,hours_ahead,itens_do_meta,search_form,search,contact,thanks

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sitetest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', hello),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^meta/$', itens_do_meta),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
    url(r'^contact/$', contact),
    url(r'^contact/thanks/$', thanks),

)
