from django.db import models

class Pancake(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()

    def __repr__(self):
        return f'{self.name}({self.price}, {self.description})'

class Order(models.Model):
    street = models.CharField(max_length=200)
    house_number = models.IntegerField()
    apartment_number = models.IntegerField()
    order_list = models.CharField(max_length=200)
    comment = models.TextField()


    def __repr__(self):
        return f'{self.street} дом {self.house_number} кв {self.apartment_number}'