"""resturant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resturantapp import views

urlpatterns = [
    
    path('newproduct/', views.new_product, name='new_product'),
    path('allproducts/', views.all_product, name='all_product'),
    path('editproduct/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delproducts/<int:product_id>/', views.del_product, name='del_product'),       
    path('neworder/', views.new_order, name='new_order'),
    path('allorders/', views.all_order, name='all_order'),
    path('editorder/<int:order_id>/', views.edit_order, name='edit_order'),
    path('delorders/<int:order_id>/', views.del_order, name='del_order'), 
    path('print/<int:order_id>/', views.print, name='print')    
]
