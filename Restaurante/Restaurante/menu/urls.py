from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('adicionar/', views.adicionar_prato, name='adicionar_prato'),
    path('editar/<int:pk>/', views.editar_prato, name='editar_prato'),
    path('excluir/<int:pk>/', views.excluir_prato, name='excluir_prato'),
]
