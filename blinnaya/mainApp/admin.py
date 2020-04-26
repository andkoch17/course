from django.contrib import admin

from .models import Pancake, Order

class PancakeAdmin(admin.ModelAdmin):
    fieldset = [
        ('Название',        {'fields': ['name']}),
        ('Цена',            {'fields': ['price']}),
        ('Описание',        {'fields': ['description']})
    ]

class OrderAdmin(admin.ModelAdmin):
    fieldset = [
        ('Улица',               {'fields': ['street']}),
        ('Дом',                 {'fields': ['house_number']}),
        ('Квартира',            {'fields': ['apartment_number']}),
        ('Комментарий',         {'fields': ['comment']}),
        ('Состав заказа',       {'fields': ['order_list']})
    ]

admin.site.register(Pancake, PancakeAdmin)
admin.site.register(Order, OrderAdmin)