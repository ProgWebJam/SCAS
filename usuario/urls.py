from django.urls import path
from .views import UsuarioCreateView, UsuarioListView, UsuarioUpdateView, UsuarioDeleteView

urlpatterns = [
    path('usuario/crear/', UsuarioCreateView.as_view() , name='usuario_crear'),
    path('usuario/listar/', UsuarioListView.as_view() , name='usuario_listar'),
    path('usuario/actualizar/<int:pk>', UsuarioUpdateView.as_view(), name='usuario_actualizar'),
    path('usuario/eliminar/<int:pk>', UsuarioDeleteView.as_view(), name='usuario_eliminar'),



]