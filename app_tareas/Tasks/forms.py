from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['categoria', 'nombre', 'descripcion', 'prioridad', 'completada', 'ultima_fecha_a_presentar']