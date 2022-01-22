from django.urls import path
from .views import index , EmpresaCreateView , EmpresaListView , EmpresaUpdateView, EmpresaDeleteView, invitarUsuario

urlpatterns = [
    path('', index , name='index'),
    path('empresa/crear/', EmpresaCreateView.as_view() , name='empresa_crear'),
    path('empresa/listar/', EmpresaListView.as_view() , name='empresa_listar'),
    path('empresa/actualizar/<int:pk>', EmpresaUpdateView.as_view(), name='empresa_actualizar'),
    path('empresa/eliminar/<int:pk>', EmpresaDeleteView.as_view(), name='empresa_eliminar'),
    path('empresa/invitar_usurio/', invitarUsuario , name='invitar_usurio'),


]