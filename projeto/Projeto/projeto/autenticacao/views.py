from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistoForm
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.models import User

# View para registrar um novo utilizador
def registo(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistoForm()
    return render(request, 'registo.html', {'form': form})

# View para exibir uma página de confirmação de logout
def confirmar_logout(request):
    return render(request, 'confirmar_logout.html')

# View para exibir uma página de sucesso após o logout
def logout_sucesso(request):
    return render(request, 'logout_sucesso.html')

# View protegida que requer login
@login_required
def pagina_protegida(request):
    return render(request, 'pagina_protegida.html', {'user': request.user})

# View para exibir o perfil do utilizador logado
@login_required
def perfil(request):
    return render(request, 'perfil.html', {'user': request.user})

# View para registrar um utilizador 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo_clientes = Group.objects.get(name='Clientes')
            user.groups.add(grupo_clientes)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registo.html', {'form': form})

# View para redefinir a senha do utilizador
def redefinir_senha_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        nova_senha = request.POST.get('nova_senha')
        confirmar_senha = request.POST.get('confirmar_senha') 

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Utilizador não encontrado.")
            return render(request, 'redefinir_senha.html')

        if nova_senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'redefinir_senha.html')

        # Atualiza a senha do utilizador
        user.password = make_password(nova_senha)
        user.save()

        # Exibe uma mensagem de sucesso
        messages.success(request, "Senha redefinida com sucesso!")
        return redirect('senha_redefinida_sucesso')

    return render(request, 'redefinir_senha.html') 

# View para exibir a página de sucesso após redefinir a senha
def senha_redefinida_sucesso(request):
    return render(request, 'registration/senha_redefinida_sucesso.html')
