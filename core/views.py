from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Funcionarios.models import Funcionario


@login_required
def home(request):
    data = {}
    usuario = data['usuario'] = request.user
    todos = Funcionario.objects.all().order_by('nome')
    contem = Funcionario.objects.filter(nome__icontains='silva')
    empresa = Funcionario.objects.filter(id__in=[2])
    context = {
        'todos':todos,
        'usuario':usuario,
        'contem':contem,
        'empresa':empresa,
        
    }
    return render(request, 'core/index.html',  context, )

# Create your views here.
