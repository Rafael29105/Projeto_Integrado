from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, MenuItem
from .forms import OrderForm

# A view de criação de um pedido
@login_required
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer_name = request.user.username
            order.save()

            return redirect('order_list')
    else:
        form = OrderForm()  

    return render(request, 'orders/order_create.html', {'form': form})


@login_required
def order_list(request):
    orders = Order.objects.filter(customer_name=request.user.username)
    return render(request, 'orders/order_list.html', {'orders': orders})


# A view para atualizar um pedido 
@login_required
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)

    return render(request, 'orders/order_update.html', {'form': form, 'order': order})


# A view para excluir um pedido
@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete() 
        return redirect('order_list') 
    return render(request, 'orders/order_confirm_delete.html', {'order': order})
