from django import forms
from .models import Order


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        
        fields = ['first_name','last_name','email','postal_code','city','address']
    
        verbose_name = 'ordercreationform'
        verbose_name_plural = 'ordercreationforms'