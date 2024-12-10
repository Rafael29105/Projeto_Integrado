from django.urls import path
from . import views
from .views import login_view, logout_view, registo_view

urlpatterns = [
    path('registo/', views.registo_view, name='registo'),
    path('logout/', logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('perfil/', views.user_profile_view, name='user_profile'),
    path('editar-perfil/', views.editar_perfil_view, name='editar_perfil'),
    path('alterar-password/', views.alterar_password_view, name='alterar_password'),
]
