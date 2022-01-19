from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Empresa
from pais.models import Estado
from django.urls import reverse_lazy
from .forms import EmpresaForm

def index(request):
    return render( request,'index.html')

class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa_form.html'
    success_url = reverse_lazy('index')

def load_estados(request):
    pais_id = request.GET.get('pais')
    estados = Estado.objects.filter(pais_id=pais_id).order_by('name')
    return render(request, 'estado_dropdown_list_options.html', {'estados': estados})
