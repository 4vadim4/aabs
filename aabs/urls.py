from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aabs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
 #   url(r'^$', 'aabs.views.welcome', name='welcome'),
    url(r'^$', 'aabs.views.home', name='home'),
    url(r'^irbis/$', 'aabs.views.irbis', name='irbis'),
    url(r'^cas_nsi/$', 'aabs.views.cas_nsi', name='cas_nsi'),
    url(r'^kc/$', 'aabs.views.kc', name='kc'),
    url(r'^vik/$', 'aabs.views.vik', name='vik'),
    url(r'^login/$', 'aabs.views.login', name='login'),

    url(r'^logout/$', 'aabs.views.logout', name='logout'),
    url(r'^openlogin/$', 'django.contrib.auth.views.login', name='openlogin'),
#    url(r'^openlogin/$', 'aabs.views.openlogin', name='openlogin'),

#    url(r'^auth/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^cas_nsi_load/$', 'aabs.views.cas_nsi_load', name='cas_nsi_load'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


