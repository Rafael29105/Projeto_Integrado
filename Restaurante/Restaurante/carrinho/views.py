from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from menu.models import Prato
from .models import Carrinho, ItemCarrinho

@login_required
def visualizar_carrinho(request):
    carrinho, created = Carrinho.objects.get_or_create(user=request.user)
    return render(request, 'carrinho.html', {'carrinho': carrinho})

@login_required
def adicionar_ao_carrinho(request, prato_id):
    prato = get_object_or_404(Prato, id=prato_id)
    carrinho, created = Carrinho.objects.get_or_create(user=request.user)
    
    item, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, prato=prato)
    
    if not created:
        item.quantidade += 1
        item.save()
    
    return redirect('visualizar_carrinho')

@login_required
def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    item.delete()
    return redirect('visualizar_carrinho')

@login_required
def atualizar_quantidade(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade'))
        item.quantidade = quantidade
        item.save()
    
    return redirect('visualizar_carrinho')
