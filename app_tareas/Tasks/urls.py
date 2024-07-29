from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, TareaViewSet, EtiquetaViewSet, ComentarioViewSet

from .views import TareasNoCompletadasView

from .views import tarea_list, tarea_detail, tarea_create, tarea_update, tarea_delete


router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'tareas', TareaViewSet)
router.register(r'etiquetas', EtiquetaViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tareas-no-completadas/', TareasNoCompletadasView.as_view(), name='tareas-no-completadas'),

    
    path('', tarea_list, name='tarea_list'),
    path('tarea/<int:pk>/', tarea_detail, name='tarea_detail'),
    path('tarea/nueva/', tarea_create, name='tarea_create'),
    path('tarea/<int:pk>/editar/', tarea_update, name='tarea_update'),
    path('tarea/<int:pk>/eliminar/', tarea_delete, name='tarea_delete'),


]