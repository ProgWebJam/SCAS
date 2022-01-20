from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Empresa
from django.urls import reverse_lazy
from .forms import EmpresaForm

def index(request):
    return render( request,'index.html')

class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa_form.html'
    success_url = reverse_lazy('index')

class EmpresaListView(ListView):
    model = Empresa
    context_object_name = 'empresas'
    template_name = 'empresa/listar_empresa.html'

class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa_form.html'
    success_url = reverse_lazy('empresa_listar')

class EmpresaDeleteView(DeleteView):
    model = Empresa
    success_url = reverse_lazy('empresa_listar')




