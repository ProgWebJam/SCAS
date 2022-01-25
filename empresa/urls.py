from django.urls import path
from .views import index , EmpresaCreateView , EmpresaListView , EmpresaUpdateView, EmpresaDeleteView, invitarUsuario , load_estado, load_ciudad

urlpatterns = [
    path('', index , name='index'),
    path('empresa/crear/', EmpresaCreateView.as_view() , name='empresa_crear'),
    path('empresa/listar/', EmpresaListView.as_view() , name='empresa_listar'),
    path('empresa/actualizar/<int:pk>', EmpresaUpdateView.as_view(), name='empresa_actualizar'),
    path('empresa/eliminar/<int:pk>', EmpresaDeleteView.as_view(), name='empresa_eliminar'),
    path('empresa/invitar_usurio/', invitarUsuario , name='invitar_usurio'),
    path('ajax/load-estado/', load_estado , name='ajax_load_estado'),
    path('ajax/load-ciudad/', load_ciudad , name='ajax_load_ciudad'),


]