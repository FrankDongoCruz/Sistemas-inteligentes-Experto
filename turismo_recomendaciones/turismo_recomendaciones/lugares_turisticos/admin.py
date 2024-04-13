from django.contrib import admin

from .models import Categoria, LugarTuristico, Usuario, Comentario, Calificacion

admin.site.register(Categoria)
admin.site.register(LugarTuristico)
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Calificacion)