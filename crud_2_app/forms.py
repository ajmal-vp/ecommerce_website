
from django import forms
from django.contrib.auth.backends import BaseBackend

from crud_2_app.models import Login, Customer, Seller

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class login_Form(UserCreationForm):

    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ("username","password1","password2",'email')

class Customer_login(forms.ModelForm):


    class Meta:
        model = Customer
        fields = ("name","address","phone_no")

class Seller_login(forms.ModelForm):

    class Meta:
        model = Seller
        fields = ("name","address","phone_no","Gst_no","product_category")


