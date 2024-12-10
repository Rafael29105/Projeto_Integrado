from django import forms

class RegistroForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Nome de Utilizador",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de Utilizador'})
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        required=True,
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'})
    )
    password_confirm = forms.CharField(
        required=True,
        label="Confirmar Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Senha'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("As senhas não correspondem.")
