from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gerenciador.views.home', name='home'),
    url(r'^registros/$', 'gerenciador.views.lista', name='lista'),
    url(r'^novoregistro/$', 'gerenciador.views.novo', name='novo'),
    url(r'^registro/(?P<id_registro>\d+)/$', 'gerenciador.views.editar', name='editar'),
    # url(r'^folhadeponto/', include('folhadeponto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
