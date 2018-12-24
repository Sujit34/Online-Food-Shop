from django.forms import ModelForm
from django import forms
from .models import Order, Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_details','price']


class OrderForm(ModelForm):
    
    OPTIONS = (
        ('Confirm', 'Order Confirm'),
        ('Ready', 'Order Ready'),
        ('Send', 'Order Send')        
        
    )
    status = forms.TypedChoiceField(required=False, choices=OPTIONS, widget=forms.RadioSelect)
    product_id = forms.ModelChoiceField(queryset=Product.objects.filter(stock='1'), empty_label='')
    delivery_date = forms.DateField(required=True)
    quantity = forms.IntegerField(initial=1)

    class Meta:
        model = Order
        fields = ['name','phone','address','delivery_date','product_id','quantity','status']