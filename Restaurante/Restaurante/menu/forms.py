from django import forms
from .models import Prato

class PratoForm(forms.ModelForm):
    class Meta:
        model = Prato
        fields = ['nome', 'descricao', 'preco', 'imagem', 'categoria']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'preco': forms.NumberInput(attrs={'step': '0.01'}),
        }
