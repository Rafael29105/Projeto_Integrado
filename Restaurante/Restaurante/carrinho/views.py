from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from menu.models import Prato
from .models import Carrinho, ItemCarrinho
from django.contrib import messages

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

def metodos_pagamento(request):
    if not request.session.get('carrinho', []):
        messages.error(request, "O seu carrinho está vazio. Adicione itens ao carrinho antes de finalizar a compra.")

    return render(request, 'metodos_pagamento.html')

def confirmar_pagamento(request):
    if request.method == 'POST':
        metodo_pagamento = request.POST.get('metodo_pagamento')

        if not metodo_pagamento:
            messages.error(request, "Por favor, escolha um método de pagamento.")
            return redirect('metodos_pagamento')

        if metodo_pagamento == 'cartao_credito_debito':
            messages.success(request, "Pagamento com Cartão de Crédito/Débito realizado com sucesso.")
        elif metodo_pagamento == 'mb_way':
            messages.success(request, "Pagamento via MB Way realizado com sucesso.")
        elif metodo_pagamento == 'paypal':
            messages.success(request, "Pagamento via PayPal realizado com sucesso.")
        elif metodo_pagamento == 'transferencia':
            messages.success(request, "Transferência Bancária realizada com sucesso.")
        else:
            messages.error(request, "Método de pagamento inválido.")

        return redirect('pagamento_concluido')

    return redirect('metodos_pagamento')

def pagamento_concluido(request):
    return render(request, 'pagamento_concluido.html')