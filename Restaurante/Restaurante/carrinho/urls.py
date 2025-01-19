from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrinho, name='carrinho'),
    path('metodos-pagamento/', views.metodos_pagamento, name='metodos_pagamento'),
    path('orders/', views.orders, name='orders'),
]
