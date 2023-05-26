from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Бренд"




class Products(models.Model):

    brand = models.ForeignKey(Brand, verbose_name="Brand" , on_delete=models.CASCADE )
    name = models.CharField(max_length=100, verbose_name="Name")
    descriptions = models.TextField(verbose_name="Description")
    price = models.FloatField(verbose_name="Price", default="100")
    size = models.IntegerField(verbose_name="Size", default="35" )
    image = models.ImageField(verbose_name="Image", upload_to="Produc_img")
    gender = models.CharField(max_length=30, verbose_name="Gender")
    quant = models.IntegerField(verbose_name="Quant")
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Продукты "


class Comment(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)

    username = models.CharField(max_length=50, verbose_name="Username")
    comment = models.TextField(verbose_name="Comment")
    create_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ["-create_data"]
        verbose_name_plural = "Коментарий"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    quant = models.IntegerField()
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.products.name)
    
    class Meta:
        verbose_name_plural = "Корзина"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    quant = models.IntegerField()
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.products.name)
    
    class Meta:
        verbose_name_plural = "Order"

