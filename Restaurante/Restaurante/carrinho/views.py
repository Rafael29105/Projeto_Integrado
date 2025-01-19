from django.shortcuts import render, redirect
from .models import Item, Pedido

def carrinho(request):
    itens = Item.objects.all()
    total = sum(item.total() for item in itens)
    return render(request, 'carrinho.html', {'itens': itens, 'total': total})

def metodos_pagamento(request):
    if request.method == 'POST':
        metodo = request.POST.get('metodo_pagamento')
        pedido = Pedido.objects.create(metodo_pagamento=metodo)
        pedido.itens.set(Item.objects.all())
        pedido.save()
        return redirect('orders')

    return render(request, 'metodos_pagamento.html')

def orders(request):
    pedidos = Pedido.objects.all()
    return render(request, 'orders.html', {'pedidos': pedidos})
