from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem  
        # Define os campos que serão incluídos no formulário.
        fields = ['name', 'description', 'price', 'is_available']  
        
        # Traduz os nomes em inglês para português
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'price': 'Preço',
            'is_available': 'Disponível',
        }
        

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nome do item'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Descrição do item'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Preço'
            }),
            'is_available': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
