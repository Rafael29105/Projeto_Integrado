from django.contrib import admin
from .models import Order

# Registrando o modelo Order no admin do Django
admin.site.register(Order)

