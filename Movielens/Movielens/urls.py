from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
#
urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','principal.views.inicio'),
    url(r'^peliculas/$','principal.views.peliculas'),
    url(r'^peliculasPuntuadas/$','principal.views.peliculasPuntuadas'),
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^formpeliculas/$','principal.views.peliculasAno'),
    url(r'^formPeliculasUsuario/$','principal.views.peliculasPuntuadasPorUsuario'),
    url(r'^categorias/$','principal.views.categorias'),)

#     url(r'^buscarPuntuacionPorUsuario/$','principal.views.idUsuario'),
#     url(r'^usuarioMasPeliculasHaPuntuado/$','principal.views.usuarioMasPeliculasHaPuntuado'),)