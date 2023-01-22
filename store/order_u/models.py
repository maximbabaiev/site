from django.db import models


import order_u


# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.email} {self.password}"


class Order(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} {self.price} {self.count}"
