from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Importa as views de autenticação
from menu.views import homepage  # Importa a view da página inicial

urlpatterns = [
    path('', homepage, name='homepage'),  # Página inicial do site
    path('admin/', admin.site.urls),  # URL para o admin do Django
    path('menu/', include('menu.urls')),  # Inclui as URLs da aplicação 'menu'
    path('', include('orders.urls')),  # Inclui as URLs da aplicação 'orders'
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('autenticacao.urls')),  # URLs da app de autenticação
]
