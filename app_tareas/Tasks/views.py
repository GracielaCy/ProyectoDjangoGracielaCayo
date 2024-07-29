from rest_framework import viewsets
from .models import Categoria, Tarea, Etiqueta, Comentario
from .serializers import CategoriaSerializer, TareaSerializer, EtiquetaSerializer, ComentarioSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


# API personalizada paso 8

class TareasNoCompletadasView(APIView):
    def get(self, request):
        tareas = Tarea.objects.filter(completada=False)
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#vistas formularios clases

def tarea_list(request):
    tareas = Tarea.objects.all()
    return render(request, 'tasks/index.html', {'tareas': tareas})

def tarea_detail(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'tasks/tarea_details.html', {'tarea': tarea})

def tarea_create(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = TareaForm()
    return render(request, 'tasks/tarea_form.html', {'form': form})

def tarea_update(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tasks/tarea_form.html', {'form': form})

def tarea_delete(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tarea_list')
    return render(request, 'tasks/tarea_confirm_delete.html', {'tarea': tarea})