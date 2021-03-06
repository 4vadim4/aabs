from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns('',
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
#    url(r'^login/$', 'aabs.views.login', name='login'),
    url(r'^logout/$', 'aabs.views.logout', name='logout'),
#    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^openlogin/$', 'django.contrib.auth.views.login', name='openlogin'),
    url(r'^cas_nsi_load/$', 'aabs.views.cas_nsi_load', name='cas_nsi_load'),
    url(r'^search/$', 'aabs.views.search', name='search'),
    url(r'^select_action/$', 'aabs.views.select_action', name='select_action'),
    url(r'^edit_form/(?P<cas_object_id>\w+)/$', 'aabs.views.edit_form', name='edit_form'),
    url(r'^i18n/', include('django.conf.urls.i18n')),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


