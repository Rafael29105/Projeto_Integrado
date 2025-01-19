from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome

    def total(self):
        return self.preco * self.quantidade

class Pedido(models.Model):
    METODOS_PAGAMENTO = [
        ('paypal', 'PayPal'),
        ('transferencia', 'Transferência Bancária'),
        ('mbway', 'MB Way'),
        ('cartao_credito', 'Cartão de Crédito'),
    ]

    itens = models.ManyToManyField(Item)
    metodo_pagamento = models.CharField(max_length=20, choices=METODOS_PAGAMENTO)
    data_pedido = models.DateTimeField(auto_now_add=True)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido #{self.id} - {'Pago' if self.pago else 'Pendente'}"
