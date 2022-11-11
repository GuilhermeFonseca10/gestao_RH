
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include
from rest_framework import routers
from Funcionarios.api.viewsets import FuncionarioViewSet

router = routers.DefaultRouter()
router.register(r'funcionario', FuncionarioViewSet)

urlpatterns = [
    path('funcionario/', include(router.urls)),
    path('', include('core.urls')),
    path('funcionarios/', include('Funcionarios.urls')),
    path('empresa/', include('empresa.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]
