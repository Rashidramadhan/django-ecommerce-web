from django.db import models

# Create your models here.
class Newuser(models.Model):
    username = models.CharField(max_length=120)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=8)
    remember_me = models.BooleanField(default=True)

class Brand(models.Model):
    brandID = models.CharField(max_length=20, default='new')
    name = models.CharField(max_length=20)

class Product_type(models.Model):
    product_typeID = models.CharField(max_length=20, default='pro')
    name = models.CharField(max_length=30)


class Product(models.Model):
    product_code = models.CharField(max_length=20, default='p001')
    product_image = models.ImageField(upload_to='images/', blank=True)
    product_name = models.CharField(max_length=20)
    product_price = models.CharField(max_length=30)
    product_description = models.TextField()
    brandID = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_typeID = models.ForeignKey(Product_type, on_delete=models.CASCADE)

class User(models.Model):
    userID = models.CharField(max_length=20, default='user')
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    admin = models.BooleanField(default=False)

class Order(models.Model):
    orderID = models.CharField(max_length=20, default='order1')
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    billing_address = models.CharField(max_length=30)
    delivery_address = models.CharField(max_length=30)
    comments = models.TextField()
    state = models.CharField(max_length=60)



class Order_product(models.Model):
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    variant = models.IntegerField()
    amount = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

class Payment(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    state = models.CharField(max_length=20)

class Order_history(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    state = models.CharField(max_length=20)

class Delivery_option(models.Model):
    name = models.CharField(max_length=20)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    state = models.CharField(max_length=20)

class Stock_level(models.Model):
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.IntegerField()
    amount = models.CharField(max_length=30)