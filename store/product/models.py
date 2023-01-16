from django.db import models
import base64


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    base_64 = models.TextField(blank=True)
    image = models.ImageField(upload_to="store/product/static/image")

    def __str__(self):
        return f"{self.name} {self.description}"

    def save(self, *args, **kwargs):
        self.base_64 = base64.b64encode(self.image.read()).decode('utf-8')
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="store/product/static/image")
    base64 = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.price}"

    def save(self, *args, **kwargs):
        self.base64 = base64.b64encode(self.image.read()).decode('utf-8')
        super(Product, self).save(*args, **kwargs)
