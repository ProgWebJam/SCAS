from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Turno
from django.urls import reverse_lazy
from .forms import TurnoForm
from django.contrib.auth.decorators import login_required


class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turno/turno_form.html'
    success_url = reverse_lazy('turno_listar')


class TurnoListView(ListView):
    model = Turno
    context_object_name = 'turnos'
    template_name = 'turno/listar_turno.html'


class TurnoUpdateView(UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turno/turno_form.html'
    success_url = reverse_lazy('turno_listar')


class TurnoDeleteView(DeleteView):
    model = Turno
    success_url = reverse_lazy('turno_listar')