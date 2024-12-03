from django.urls import path
from . import views

urlpatterns = [
    # URL para a página protegida (requer autenticação ou permissões específicas)
    path('pagina-protegida/', views.pagina_protegida, name='pagina_protegida'),
    # URL para a página de registro de novos utilizadores
    path('registo/', views.registo, name='registo'),
    # URL para confirmar se o utilizador deseja fazer logout
    path('confirmar-logout/', views.confirmar_logout, name='confirmar_logout'),
    # URL para redirecionar após o logout bem-sucedido
    path('logout-sucesso/', views.logout_sucesso, name='logout_sucesso'),  
    # URL para a página de perfil do utilizador
    path('perfil/', views.perfil, name='perfil'),  
    # URL para a página de redefinição de senha
    path('redefinir-senha/', views.redefinir_senha_view, name='redefinir_senha'),
    # URL para redirecionar após a senha ser redefinida com sucesso
    path('senha-redefinida-sucesso/', views.senha_redefinida_sucesso, name='senha_redefinida_sucesso'),
]
