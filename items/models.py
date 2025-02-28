from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def price_in_dollars(self):
        return int(self.price * 100)


class Order(models.Model):
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f"Order {self.id}"

    def total_price(self):
        # Вычисляем общую стоимость всех товаров в заказе
        return sum(item.price for item in self.items.all())
