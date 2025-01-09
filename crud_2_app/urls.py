from django.urls import path

from crud_2_app import views

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

    # path('add',views.add, name="add"),
]