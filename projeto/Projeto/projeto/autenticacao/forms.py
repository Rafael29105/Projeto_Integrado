from django import forms
from django.contrib.auth.models import User
import re  # Certifique-se de importar o módulo re

class RegistoForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text="O nome de utilizador deve ter no máximo 150 caracteres e pode conter letras, números, e os caracteres @/./+/-/_."
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        help_text=(
            "A senha deve cumprir pelo menos 3 dos seguintes requisitos: "
            "Caracter minúsculo, Caracter maiúsculo, Número, "
            "Caracter especial."
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está registrado. Por favor, utilize outro.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        # Requisitos da senha
        has_lowercase = bool(re.search(r'[a-z]', password))
        has_uppercase = bool(re.search(r'[A-Z]', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        has_digit = bool(re.search(r'\d', password))

        # Verificar se pelo menos 3 requisitos são cumpridos
        conditions_met = sum([has_lowercase, has_uppercase, has_special, has_digit])
        if conditions_met < 3:
            raise forms.ValidationError(
                "A senha deve cumprir pelo menos 3 dos seguintes requisitos: "
                "Caracter minúsculo, Caracter maiúsculo, Número, "
                "Caracter especial."
            )
        return password
