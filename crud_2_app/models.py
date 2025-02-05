from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

class Customer(models.Model):
    customer_data = models.ForeignKey("login",on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=10)





class Seller(models.Model):
    seller_data = models.ForeignKey('Login',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=12)
    Gst_no = models.CharField(max_length=10)

    product_category = models.CharField(max_length=100)

class product(models.Model):
    product_user = models.ForeignKey("Seller",on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=20)
    quantity = models.IntegerField()
    product_description = models.CharField(max_length=400)
    product_price = models.CharField(max_length=4)
    product_image = models.FileField(upload_to="images/")

class cart(models.Model):
    product_data = models.ForeignKey("product",on_delete=models.DO_NOTHING)
    customer_data = models.ForeignKey("Customer",on_delete=models.DO_NOTHING)

class buy_now(models.Model):
    product = models.ForeignKey('product',on_delete=models.DO_NOTHING)
    customer = models.ForeignKey('Customer',on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=0)
    status = models.IntegerField(default=0)


class pay_now(models.Model):
    buy_id = models.ForeignKey('buy_now',on_delete=models.DO_NOTHING)
    card_no = models.CharField(max_length=12)
    CVV = models.CharField(max_length=3)
    expiry_date = models.DateField()






