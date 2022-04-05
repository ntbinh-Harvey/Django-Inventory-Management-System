from winreg import REG_OPTION_CREATE_LINK
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Books', 'Books'),
    ('Mobile Phones', 'Mobile Phones'),
    ('Clothes', 'Clothes'),
    ('Laptop', 'Laptop'),
    ('Shoes', 'Shoes'),
    ('Electronics', 'Electronics'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    images = models.ImageField(upload_to='photos/products')
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'
