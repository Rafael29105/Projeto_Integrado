from django.urls import path
from .views import menu_list, menu_create, menu_update, menu_delete, homepage

urlpatterns = [
    # Define a URL para a listagem de itens do menu
    path('menu/', menu_list, name='menu_list'),
    # Define a URL para a criação de um novo item no menu
    path('menu/create/', menu_create, name='menu_create'),
    # Define a URL para a atualização de um item do menu
    path('menu/<int:pk>/update/', menu_update, name='menu_update'),
    # Define a URL para a exclusão de um item do menu
    path('menu/<int:pk>/delete/', menu_delete, name='menu_delete'),
]
