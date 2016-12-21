#enconding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','principal.views.inicio'),
    url(r'^buscaPuntuacionPorUsuario/$','principal.views.buscaPuntuacionesUsuarios'),)
#     url(r'^buscarPuntuacionPorUsuario/$','principal.views.idUsuario'),
#     url(r'^usuarioMasPeliculasHaPuntuado/$','principal.views.usuarioMasPeliculasHaPuntuado'),)