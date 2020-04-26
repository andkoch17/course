from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mainApp.models import Pancake
from .cart import Cart
from .forms import CartAddPancakeForm


@require_POST
def cart_add(request, pancake_id):
    cart = Cart(request)
    pancake = get_object_or_404(Pancake, id=pancake_id)
    form = CartAddPancakeForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(pancake=pancake, amount=cd['amount'], update_amount=cd['update'])
        return redirect('cart:cart_detail')

def cart_remove(request, pancake_id):
    cart = Cart(request)
    pancake = get_object_or_404(Pancake, id=pancake_id)
    cart.remove(pancake)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

