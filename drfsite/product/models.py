from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.CharField(max_length=100)
    is_stock = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    shop = models.ForeignKey('Shop', on_delete=models.PROTECT, null=True, default=1)

    def __str__(self):
        return self.name
