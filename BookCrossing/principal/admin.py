#enconding:utf-8
from principal.models import Libro,  Usuario, Puntuacion
from django.contrib import admin

admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Puntuacion)