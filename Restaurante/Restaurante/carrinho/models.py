# carrinho/models.py
from django.db import models
from django.contrib.auth.models import User
from menu.models import Prato  # Supondo que o modelo Prato está na app 'menu'

class Carrinho(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carrinho')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrinho de {self.user.username}'

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name='itens', on_delete=models.CASCADE)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return self.quantidade * self.prato.preco

    def __str__(self):
        return f'{self.quantidade} x {self.prato.nome}'
