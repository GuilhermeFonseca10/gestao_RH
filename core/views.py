from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from Funcionarios.models import Funcionario

@login_required
def home(request):
    
    #todos = Funcionario.objects.all()
    #context = {
        #'todos':todos,
    #}
    return render(request, 'core/index.html',) #context, )

# Create your views here.
