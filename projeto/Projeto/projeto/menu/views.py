from django.contrib.auth.decorators import login_required, permission_required, user_passes_test 
from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem
from .forms import MenuItemForm

# Helper para verificar se o utilizador é gerente ou administrador.
def is_manager(user):
    return user.is_staff or user.is_superuser

# View para a página inicial (homepage).
def homepage(request):
    return render(request, 'homepage.html')

# Listar itens do menu
@login_required
@permission_required('menu.view_menuitem', raise_exception=True)
def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {
        'menu_items': menu_items,
        'is_admin': request.user.is_superuser,
    })

# Criar novo item do menu
@login_required
@user_passes_test(is_manager)
def menu_create(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'menu/menu_form.html', {'form': form, 'action': 'Criar Novo Item'})

# Atualizar item do menu
@login_required
@user_passes_test(is_manager)
def menu_update(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'menu/menu_form.html', {'form': form, 'action': 'Editar Item'})

# Eliminar item do menu
@login_required
@user_passes_test(is_manager)
def menu_delete(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('menu_list')
    return render(request, 'menu/menu_delete.html', {'item': item})
