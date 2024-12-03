from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'menu_item', 'quantity', 'status']  # Define os campos do modelo que serão usados no formulário.
        labels = {  # Tradução do Inglês para o Português
            'customer_name': 'Nome do Cliente',
            'menu_item': 'Item do Menu',
            'quantity': 'Quantidade',
            'status': 'Estado',
        }
