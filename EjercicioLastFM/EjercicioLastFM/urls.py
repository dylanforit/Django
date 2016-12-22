from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),  
    url(r'^$','principal.views.inicio'),
    url(r'^artistasPorUsuario/$','principal.views.artistasPorUsuario'),
    
    
)