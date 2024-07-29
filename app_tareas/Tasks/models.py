from django.db import models
from django.core.exceptions import ValidationError

def validar_prioridad(value):
    if value < 1 or value > 5:
        raise ValidationError('La prioridad debe estar entre 1 y 5.')

def validar_no_vacio(value):
    if not value.strip():
        raise ValidationError('Este campo no puede estar vacío.')

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='tareas', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, validators=[validar_no_vacio])
    descripcion = models.TextField(validators=[validar_no_vacio])
    prioridad = models.IntegerField(validators=[validar_prioridad])
    completada = models.BooleanField(default=False)
    ultima_fecha_a_presentar = models.DateTimeField()

    def __str__(self):
        return self.nombre[:20]

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    tarea = models.ForeignKey(Tarea, related_name='comentarios', on_delete=models.CASCADE)
    texto = models.TextField(validators=[validar_no_vacio])
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:20]