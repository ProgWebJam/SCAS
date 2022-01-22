from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Empresa
from django.urls import reverse_lazy
from .forms import EmpresaForm
from django.contrib.auth.decorators import login_required

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

@login_required(login_url='/accounts/acceder')
def index(request):
    return render( request,'index.html')

def send_email(mail):
    #print(mail)
    context = { 'mail' : mail }
    template = get_template('correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Un correo de prueba',
        'Invitacion usuario a registrarse',
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content,'text/html')
    email.send()

def invitarUsuario(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_email(mail)
    return render( request,'empresa/enviar_correo.html')


class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa_form.html'
    success_url = reverse_lazy('index')


class EmpresaListView(ListView):
    model = Empresa
    context_object_name = 'empresas'
    template_name = 'empresa/listar_empresa.html'
    queryset = Empresa.objects.all()
    paginate_by = 3


class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa/empresa_form.html';
    success_url = reverse_lazy('empresa_listar')


class EmpresaDeleteView(DeleteView):
    model = Empresa
    success_url = reverse_lazy('empresa_listar')




