from django.core.validators import MinValueValidator
from django.db import models
from menu.models import MenuItem

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    
    # Campo que cria uma relação de chave estrangeira com o modelo MenuItem.
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)  
    
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    # O validador 'MinValueValidator(0)' garante que a quantidade não será negativa 
    
    status = models.CharField(max_length=50)  # Campo para armazenar o estado do pedido 
    
    def __str__(self):
        # Retorna uma string formatada com o nome do cliente e o nome do item do menu associado.
        return f"{self.customer_name} - {self.menu_item.name}"
    
    @property
    def total_price(self):
        # Propriedade que calcula o preço total do pedido (preço do item * quantidade).
        return self.menu_item.price * self.quantity
