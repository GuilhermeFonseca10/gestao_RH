from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Funcionarios.models import Funcionario


@login_required
def home(request):
    data = {}
    usuario = data['usuario'] = request.user
    
    context = {
     
        'usuario':usuario,
        
    }
    return render(request, 'core/index.html',  context, )

def atividade(request):
    todos = Funcionario.objects.all().order_by('nome')
    contem = Funcionario.objects.filter(nome__icontains='silva')
    empresa = Funcionario.objects.filter(id__in=[2])

    context = {
        'todos':todos,
        'contem':contem,
        'empresa':empresa,
        
    }
    return render(request, 'core/atividade.html',  context, )
# Create your views here.
