from django.shortcuts import render, redirect, get_object_or_404
from .models import Prato
from .forms import PratoForm
from django.contrib.auth.decorators import login_required, permission_required

def menu(request):
    categorias = [
        'Entradas', 'Sopas', 'Carne', 'Peixe', 
        'Sobremesas', 'Sumos', 'Vinhos', 'Cafés'
    ]
    
    pratos_por_categoria = {}

    for categoria in categorias:
        pratos = Prato.objects.filter(categoria=categoria)
        pratos_por_categoria[categoria] = pratos
    
    is_gerente = request.user.groups.filter(name='Gerente').exists()
    print(pratos_por_categoria)
    return render(request, 'menu.html', {
        'pratos_por_categoria': pratos_por_categoria, 
        'is_gerente': is_gerente
    })

@login_required
@permission_required('menu.add_prato', raise_exception=True)
def adicionar_prato(request):
    if request.method == 'POST':
        form = PratoForm(request.POST, request.FILES)
        if form.is_valid():
            prato = form.save(commit=False)
            prato.save()  # Salva o prato no banco de dados
            return redirect('menu')  # Redireciona para a página do menu
    else:
        form = PratoForm()  # Cria um formulário vazio para o método GET

    return render(request, 'adicionar_prato.html', {'form': form})

@login_required
@permission_required('menu.change_prato', raise_exception=True)
def editar_prato(request, pk):
    prato = get_object_or_404(Prato, pk=pk)
    if request.method == 'POST':
        form = PratoForm(request.POST, request.FILES, instance=prato)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = PratoForm(instance=prato)

    return render(request, 'editar_prato.html', {'form': form, 'prato': prato})

@login_required
@permission_required('menu.delete_prato', raise_exception=True)
def excluir_prato(request, pk):
    prato = get_object_or_404(Prato, pk=pk)
    prato.delete()
    return redirect('menu')
