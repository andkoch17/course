from django.shortcuts import render, redirect

from .models import Pancake, Order
from cart.forms import CartAddPancakeForm
from cart.cart import Cart


def index(request):
    if request.method == 'GET':
        pancakes = Pancake.objects.all()
        cart_pancake_form = CartAddPancakeForm()
        return render(request, 'mainApp/index.html', {'pancakes': pancakes, 'cart_pancake_form': cart_pancake_form})


def make_order(request):
    if request.method == 'GET':
        return render(request, 'mainApp/make_order.html')
    elif request.method == 'POST':
        street = request.POST['street']
        house_number = int(request.POST['house_number'])
        apartment_number = int(request.POST['apartment_number'])
        comment = request.POST['comment']
        cart = Cart(request).cart
        order_list = ''
        for item in cart.keys():
            order_list += f'{item}-{cart[item]["amount"]},'
        new_order = Order(street=street, house_number=house_number, apartment_number=apartment_number,
                            comment=comment, order_list=order_list)
        new_order.save()
        return redirect(f'mainApp:wait', order_id = new_order.id)


def contact(request):
    return render(request, 'mainApp/contact.html')


def wait(request, order_id):
    return render(request, 'mainApp/wait_page.html', {'order_id': order_id})