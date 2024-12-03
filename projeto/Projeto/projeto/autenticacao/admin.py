from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.apps import apps

#Registar o grupo "Clientes" com permissões personalizadas
clientes_group, created = Group.objects.get_or_create(name="Clientes")
if created:
    Order = apps.get_model('orders', 'Order')
    permission = Permission.objects.get(codename='ver pedido')
    clientes_group.permissions.add(permission)