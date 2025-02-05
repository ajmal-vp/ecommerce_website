from itertools import count

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request


from crud_2_app.filters import BrandFilter
from crud_2_app.forms import pay_now_form
from crud_2_app.models import product, cart, Customer, buy_now


def view_product(request):

    data = product.objects.all()
    brand_filter = BrandFilter(request.GET,queryset=data)
    data = brand_filter.qs

    return render(request,"customer/view_product.html",{"data":data,"brand_filter":brand_filter})

def add_to_cart(request,id):
    user_data = request.user
    product_data = product.objects.get(id=id)
    customer_data1 = Customer.objects.get(customer_data = user_data)
    addto_cart = cart.objects.filter(product_data=product_data,customer_data=customer_data1)
    print(addto_cart)
    if addto_cart.exists():
        messages.info(request,'item is already added to cart!')
        return redirect('view_product')


    else:
        obj = cart()
        obj.product_data = product_data
        obj.customer_data = customer_data1
        obj.save()
        messages.info(request,'product added to cart')
        return redirect('view_product')


    return render(request, 'customer/view_product.html',{"user_data":user_data})

def cart_view(request):
    user = request.user
    customer_data1 = Customer.objects.get(customer_data=user)
    data = cart.objects.filter(customer_data=customer_data1)

    return render(request,'customer/view_cart.html',{'data':data})

def delete_cart(request,id):
    data = cart.objects.get(id=id)
    print(data)
    data.delete()
    return redirect('cart_view')


    return render(request,'customer/view_cart.html')

def buy_product_cart(request,id):

    cart_data = cart.objects.get(id=id)
    print(cart_data.product_data)
    product_data =cart_data.product_data

    if request.method == 'POST':
        user_data = request.user
        print(user_data)
        customer_data1 = Customer.objects.get(customer_data = user_data)
        print()
        count = request.POST.get('count')

        obj = buy_now(customer = customer_data1,count = count,product = product_data )
        obj.save()
        return redirect('order_summary')


    return render(request,"customer/buy_now_cart.html",{'data':product_data})

def buy_product(request,id):
    product_data = product.objects.get(id = id)
    if request.method == 'POST':
        user_data = request.user
        print(user_data)
        customer_data1 = Customer.objects.get(customer_data = user_data)
        print(customer_data1)
        count = request.POST.get('count')
        print(count)

        obj = buy_now(customer = customer_data1,count= count,product=product_data)
        obj.save()
        return redirect('order_summary')


    return render(request,'customer/buy_now.html',{'data':product_data})

def order_summary(request, id):

    data = buy_now.objects.all()
    customer = Customer.objects.filter(customer_data=request.user)


    return render(request, "customer/order_summary.html", {'data': data})

def pay_now(request,id):
    order = buy_now.objects.get(id = id)
    if request.method=='POST':
        form = pay_now_form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.buy = order
            obj.save()

    else:
        form = pay_now_form()

    return render(request,'customer/pay_now.html',{'form': form,'order':order})





