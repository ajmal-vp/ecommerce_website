from django.shortcuts import redirect, render

from crud_2_app.forms import product_form
from crud_2_app.models import product, Seller


def product_upload(request):

    user_data = request.user
    seller_data = Seller.objects.get(seller_data=user_data)

    if request.method == 'POST':

        form = product_form(request.POST, request.FILES)
        if form.is_valid():

            obj =  form.save(commit=False)
            obj.product_user = seller_data
            obj.save()
            return redirect("product_details")
    else:
        form = product_form()
    return render(request, 'seller/product_upload.html', {'form': form})


def product_details(request):

    user = request.user
    seller_data1 = Seller.objects.get(seller_data = user)
    data = product.objects.filter(product_user = seller_data1)

    return render(request,"seller/view_product.html",{"data":data})