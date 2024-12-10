from django import forms
from .models import Prato

class PratoForm(forms.ModelForm):
    class Meta:
        model = Prato
        fields = ['nome', 'descricao', 'preco', 'imagem', 'categoria']
        labels = {
            'nome': 'Nome do Prato',
            'descricao': 'Descrição',
            'preco': 'Preço (€)',
            'imagem': 'Imagem do Prato',
            'categoria': 'Categoria',
        }
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do prato'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva o prato brevemente'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Exemplo: 12.50'
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        help_texts = {
            'nome': 'Insira o nome do prato de forma clara.',
            'preco': 'Digite o preço no formato decimal. Exemplo: 12.50',
        }
        error_messages = {
            'nome': {
                'required': 'O nome do prato é obrigatório.',
                'max_length': 'O nome do prato não pode ter mais de 100 caracteres.',
            },
            'preco': {
                'invalid': 'Por favor, insira um valor numérico válido para o preço.',
            },
        }

    # Validação personalizada para o campo preco
    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco is not None and preco < 0:
            raise forms.ValidationError("O preço não pode ser negativo. Insira um valor válido.")
        return preco
