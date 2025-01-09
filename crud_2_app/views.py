from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from crud_2_app.forms import Customer_login, Seller_login, login_Form


# Create your views here.

def home(request):
    return render(request, 'index.html')

def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

def seller_dashboard(request):
    return render(request, 'seller/seller_dashboard.html')
def customer_dashboard(request):
    return render(request, 'customer/customer_dashboard.html')




def login_form(request):
    form = login_form()
    print(form)

    # if request.method == 'POST':
    #     data = Customer_login_Form(request.POST)
    #     if data.is_valid():
    #         data.save()


    return render(request,"login_form.html",{"form":form})






def customer_add(request):
    login_form1 = login_Form()
    customer_form = Customer_login()

    if request.method == 'POST':
        customer_form = Customer_login(request.POST)
        login_form1 = login_Form(request.POST)

        if customer_form.is_valid() and login_form1.is_valid():
            customer = login_form1.save(commit=False)
            customer.is_customer = True
            customer.save()

            user = customer_form.save(commit=False)
            user.customer_data = customer
            user.save()

            return redirect('customer_add')

    return render(request,'customer/register.html',{'customer_form':customer_form,'login_form':login_form1})

def seller_add(request):
    login_form2 = login_Form()
    seller_form = Seller_login()

    if request.method == 'POST':
        seller_form = Seller_login(request.POST)
        login_form2 = login_Form(request.POST)

        if seller_form.is_valid() and login_form2.is_valid():
            seller = login_form2.save(commit=False)
            seller.is_seller = True
            seller.save()

            user = seller_form.save(commit=False)
            user.seller_data = seller
            user.save()

            return redirect('customer_add')

    return render(request, 'seller/seller_login.html', {'seller_form': seller_form, 'login_form': login_form2})


def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_dashboard')
            elif user.is_customer:
                return redirect('customer_dashboard')
            elif user.is_seller:
                return redirect('seller_dashboard')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,"login.html")



