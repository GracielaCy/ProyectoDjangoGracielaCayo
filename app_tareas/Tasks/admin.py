from django.contrib import admin
from .models import Categoria, Tarea, Comentario, Etiqueta 

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tarea)
admin.site.register(Etiqueta)
admin.site.register(Comentario)

