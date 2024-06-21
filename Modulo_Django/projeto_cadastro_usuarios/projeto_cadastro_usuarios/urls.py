from django.urls import path, include
from app_cadastro_usuarios import views

urlpatterns = [
    # other URL patterns
# rota, view responsável, nome de referência
#     # usuarios.com
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('__debug__/', include('debug_toolbar.urls')),
]