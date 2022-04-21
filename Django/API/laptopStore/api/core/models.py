from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    img = models.ImageField(blank=True, null=True)
    default_address = models.TextField(blank=True, null=True)
    ship_address = models.TextField(blank=True, null=True)


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255)
    img = models.ImageField(blank=True, null=True)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, default=None)
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    img = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    total = models.FloatField(default=0)
    num = models.IntegerField(default=0)


class CartDetail(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=None)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    quantity = models.IntegerField(default=0)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    status = models.CharField(max_length=255, blank=True, null=True)


class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, default=None)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=None)
    quantity = models.IntegerField(default=0)


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15)
    content = models.TextField()
