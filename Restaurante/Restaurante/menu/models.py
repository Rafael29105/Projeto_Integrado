from django.db import models

class Prato(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='media/')
    categoria = models.CharField(
        max_length=50,
        choices=[
            ('Entradas', 'Entradas'),
            ('Sopas', 'Sopas'),
            ('Carne', 'Pratos de Carne'),
            ('Peixe', 'Pratos de Peixe'),
            ('Sobremesas', 'Sobremesas'),
            ('Sumos', 'Sumos'),
            ('Vinhos', 'Vinhos'),
            ('Cafés', 'Cafés'),
        ]
    )

    def __str__(self):
        return self.nome
