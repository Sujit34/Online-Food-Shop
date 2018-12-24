from django.shortcuts import render, redirect
from .models import Order, Product
from .forms import OrderForm, ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


# Add new Product
@login_required
def new_product(request):
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/allproducts', messages.success(request, 'Product was successfully created.', 'alert-success'))
            else:
                return redirect('/allproducts', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/allproducts', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        product_form = ProductForm()
        return render(request, 'new_product.html', {'product_form':product_form})


#Show all products
@login_required
def all_product(request):
    products = Product.objects.filter(stock='1')
    return render(request, 'all_products.html', {'products': products})


#Delete products
@login_required
def del_product(request, product_id):
    if Product.objects.filter(id=product_id).update(stock='0'):
        return redirect('/allproducts', messages.success(request, 'Successfully Deleted', 'alert-success'))
    else:
        return redirect('/allproducts', messages.error(request, 'can not delete the product', 'alert-danger'))


# Edit Product
@login_required
def edit_product(request, product_id):
    product= Product.objects.get(id=product_id)
    if request.POST:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            if form.save():
                return redirect('/allproducts', messages.success(request, 'Product was successfully updated.', 'alert-success'))
            else:
                return redirect('/allproducts', messages.error(request, 'Data is not updated', 'alert-danger'))
        else:
            return redirect('/allproducts', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        product_form = ProductForm(instance=product)
        return render(request, 'new_product.html', {'product_form':product_form})
    
       
    
# Add new Order
@login_required
def new_order(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/allorders', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/allorders', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/allorders', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        order_form = OrderForm()
        return render(request, 'new_order.html', {'order_form':order_form})



#Show all Orders
@login_required
def all_order(request):
    orders = Order.objects.all()
    return render(request,'all_orders.html', {'orders': orders})


#Delete Products
def del_order(request, order_id):
    if Order.objects.filter(id=order_id).delete():
        return redirect('/allorders', messages.success(request, 'Successfully Deleted', 'alert-success'))
    else:
        return redirect('/allorders', messages.error(request, 'can not delete the product', 'alert-danger'))


# Edit Order
@login_required
def edit_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect('/allorders', messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect('/allorders', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/allorders', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        order_form = OrderForm(instance=order)
        return render(request, 'new_order.html', {'order_form':order_form})

#print Invoice
def print(request,order_id):
    order = Order.objects.filter(id=order_id)
    return render(request,'print.html', {'order': order})