from django.urls import path
from .views import index, load_estados
from .views import EmpresaCreateView

urlpatterns = [
    path('', index , name='index'),
    path('empresa_crear/', EmpresaCreateView.as_view() , name='empresa_crear'),
    path('ajax/load-estados/', load_estados, name='ajax_load_estados'),

]