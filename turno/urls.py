from django.urls import path
from .views import TurnoCreateView, TurnoListView, TurnoUpdateView, TurnoDeleteView

urlpatterns = [
    path('turno/crear/', TurnoCreateView.as_view() , name='turno_crear'),
    path('turno/listar/', TurnoListView.as_view() , name='turno_listar'),
    path('turno/actualizar/<int:pk>', TurnoUpdateView.as_view(), name='turno_actualizar'),
    path('turno/eliminar/<int:pk>', TurnoDeleteView.as_view(), name='turno_eliminar'),



]