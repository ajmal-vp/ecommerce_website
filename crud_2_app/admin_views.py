from crud_2_app import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from crud_2_app.filters import SellerFilter
from crud_2_app.forms import login_Form,Customer_login,Seller_login
from crud_2_app.models import Customer, Seller, product
from crud_2_app.views import seller_add


def customer_details(request):
    data = Customer.objects.all()
    print(data)

    return render(request ,"admin/customer_details.html" ,{"data" :data})

def seller_details(request):
    data = Seller.objects.all()
    print(data)

    return render(request ,"admin/seller_details.html" ,{"data" :data})

def delete_customer(request,id):
    data = Customer.objects.get(id=id)
    print(data)
    data.delete()
    return redirect('customer_details')


    return render(request,'admin/customer_details.html')

def update_seller(request,id):
    data = Seller.objects.get(id=id)

    form1 = Seller_login(instance=data)


    if request.method == 'POST':
        data = Seller_login(request.POST,instance= data)
        if data.is_valid():
            data.save()
            return redirect("seller_details")

    return render(request,"seller/seller_login.html",{"seller_form":form1})

def view_product_admin(request):

    data = product.objects.all()
    seller_filter = SellerFilter(request.GET,queryset=data)
    data = seller_filter.qs

    return render(request,"admin/view_product.html",{"data":data,'seller_filter':seller_filter})