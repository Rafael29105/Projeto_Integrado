# carrinho/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualizar_carrinho, name='visualizar_carrinho'),
    path('adicionar/<int:prato_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('atualizar/<int:item_id>/', views.atualizar_quantidade, name='atualizar_quantidade'),
]
