from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Sede
from django.urls import reverse_lazy
from .forms import SedeForm
from django.contrib.auth.decorators import login_required


class SedeCreateView(CreateView):
    model = Sede
    form_class = SedeForm
    template_name = 'sede/sede_form.html'
    success_url = reverse_lazy('sede_listar')


class SedeListView(ListView):
    model = Sede
    context_object_name = 'sedes'
    template_name = 'sede/listar_sede.html'
    queryset = Sede.objects.all()
    paginate_by = 3


class SedeUpdateView(UpdateView):
    model = Sede
    form_class = SedeForm
    template_name = 'sede/sede_form.html'
    success_url = reverse_lazy('sede_listar')


class SedeaDeleteView(DeleteView):
    model = Sede
    success_url = reverse_lazy('sede_listar')

