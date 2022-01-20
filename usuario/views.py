from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Usuario
from django.urls import reverse_lazy
from .forms import UsuarioForm

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario_listar')

class UsuarioListView(ListView):
    model = Usuario
    context_object_name = 'usuarios'
    template_name = 'usuario/listar_usuario.html'

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario_listar')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario_listar')
