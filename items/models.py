from django.db import models


class Discount(models.Model):
    amount = models.IntegerField(help_text="Скидка в процентах")
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.amount}% Discount"


class Tax(models.Model):
    rate = models.IntegerField(help_text="Налоговая ставка в прцоентах")
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.rate}% Tax"


class Item(models.Model):
    CURRENCY_CHOISE = [
        ('usd', 'USD'),
        ('rub', 'RUB')
    ]
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOISE, default='usd')

    def __str__(self):
        return self.name

    def price_in_dollars(self):
        return int(self.price * 100)


class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id}"

    def total_price(self):
        total = sum(item.price for item in self.items.all())
        if self.discount:
            total == total * self.discount.amount /100
        if self.tax:
            total += total * self.tax.rate / 100
        return int(total)

