from django.urls import path
from .views import home
from .views import atividade

urlpatterns = [
    path('', home, name='home'),
    path('atividade/', atividade, name='atividade'),
]