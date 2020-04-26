from decimal import Decimal
from django.conf import settings
from mainApp.models import Pancake

class Cart():
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, pancake, amount=1, update_amount=False):
        pancake_id = str(pancake.id)
        if pancake_id not in self.cart.keys():
            from time import sleep
            print('zalupa konya')
            sleep(5)
            self.cart[pancake_id] = {
                                    'amount': 0,
                                    'price': str(pancake.price)
                                    }
        
        if update_amount:
            self.cart[pancake_id]['amount'] = amount
        else:
            self.cart[pancake_id]['amount'] += amount
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, pancake):
        pancake_id = str(pancake.id)
        if pancake_id in self.cart:
            del self.cart[pancake_id]
            self.save()

    def __iter__(self):
        pancake_ids = self.cart.keys()
        pancakes = Pancake.objects.filter(id__in=pancake_ids)
        for pancake in pancakes:
            self.cart[str(pancake.id)]['pancake'] = pancake

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['amount']
            yield item

    def __len__(self):
        return sum(item['amount'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['amount'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True