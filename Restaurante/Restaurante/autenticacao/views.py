from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegistroForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Profile

def registo_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                messages.error(request, "O nome de utilizador já está em uso.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "O email já está registrado.")
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "Conta criada com sucesso! Faça login.")
                return redirect('login')
    else:
        form = RegistroForm()

    return render(request, 'autenticacao/registo.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bem-vindo(a), {user.username}!")
            return redirect('homepage')  # Redirecionar para a homepage ou outra página desejada
        else:
            messages.error(request, "Nome de utilizador ou senha inválidos.")
    
    return render(request, 'autenticacao/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'homepage.html')

@login_required
def user_profile_view(request):
    return render(request, 'autenticacao/user_profile.html')

@login_required
def editar_perfil_view(request):
    if request.method == 'POST':
        user = request.user

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        profile, created = Profile.objects.get_or_create(user=user)

        phone_number = request.POST.get('phone_number')
        if phone_number:
            profile.phone_number = phone_number

        user.save()
        profile.save()

        return redirect('user_profile')

    return render(request, 'autenticacao/editar_perfil.html', {'user': request.user})

def alterar_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password alterada com sucesso!')
            return redirect('user_profile.html') 
        else:
            messages.error(request, 'Erro ao alterar a password. Verifique se as passwords são válidas e tente novamente.')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'autenticacao/alterar_password.html', {'form': form})