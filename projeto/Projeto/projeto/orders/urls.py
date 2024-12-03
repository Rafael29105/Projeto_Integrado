from django.urls import path
from . import views

urlpatterns = [
    # URL para listar os pedidos
    path('orders/', views.order_list, name='order_list'),

    # URL para criar um novo pedido
    path('orders/create/', views.order_create, name='order_create'),

    # URL para atualizar um pedido
    path('orders/update/<int:pk>/', views.order_update, name='order_update'),

    # URL para excluir um pedido
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
]
