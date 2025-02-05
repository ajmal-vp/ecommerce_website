from django.urls import path

from crud_2_app import views, admin_views, seller_views, customer_views

urlpatterns = [
    path('',views.home,name="home"),

    # path('login', views.login, name="login"),


    path('login_form', views.login_form, name="login_form"),
    path('customer_add', views.customer_add, name="customer_add"),
    path('seller_add', views.seller_add, name="seller_add"),
    path('login_view',views.login_views,name='login_view'),
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('customer_dashboard', views.customer_dashboard, name="customer_dashboard"),
    path('seller_dashboard', views.seller_dashboard, name="seller_dashboard"),
    path('customer_details',admin_views.customer_details,name='customer_details'),
    path('seller_details', admin_views.seller_details, name='seller_details'),

    #delete_customer
    path('delete_customer/<int:id>/',admin_views.delete_customer,name='delete_customer'),

    path('update_seller/<int:id>/',admin_views.update_seller,name='update_seller'),
    path('product_upload',seller_views.product_upload,name='product_upload'),
    path('product_details',seller_views.product_details,name='product_details'),
    path('view-product',customer_views.view_product,name='view_product'),
    path('view-product_admin',admin_views.view_product_admin,name='view_product_admin'),
    path('add_to_cart/<int:id>/',customer_views.add_to_cart,name='add_to_cart'),
    path('cart_view',customer_views.cart_view,name='cart_view'),
    path('delete_cart/<int:id>/',customer_views.delete_cart,name='delete_cart'),
    path('buy_product/<int:id>/',customer_views.buy_product,name='buy_product'),
    path('buy_product_cart/<int:id>/', customer_views.buy_product_cart, name='buy_product_cart'),
    path('order_summary/<int:id>/', customer_views.order_summary, name='order_summary'),
    path('pay_now/<int:id>/',customer_views.pay_now,name='pay_now')



]