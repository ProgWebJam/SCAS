from django.urls import path
from .views import SedeCreateView, SedeListView, SedeUpdateView, SedeaDeleteView

urlpatterns = [
    path('sede/crear/', SedeCreateView.as_view() , name='sede_crear'),
    path('sede/listar/', SedeListView.as_view() , name='sede_listar'),
    path('sede/actualizar/<int:pk>', SedeUpdateView.as_view(), name='sede_actualizar'),
    path('sede/eliminar/<int:pk>', SedeaDeleteView.as_view(), name='sede_eliminar'),



]