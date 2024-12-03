from django.db import models  
from django.core.exceptions import ValidationError 

# Define o modelo MenuItem que representa um item de menu no banco de dados.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)  
    
    description = models.TextField()  
    
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    is_available = models.BooleanField(default=True)  

    # Método que define como o item será representado quando convertido para string.
    def __str__(self):
        return self.name

    def clean(self):
        # Verifica se o preço é negativo.
        if self.price < 0:
            # Se o preço for negativo, manda uma mensagem personalizada.
            raise ValidationError({'price': 'O preço não pode ser negativo.'})
