from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.


# product list display function
def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    
    return render(request,'shop/list.html',{'category':category,
                                            'categories':categories,
                                            'products':products})    
    
    
    


# product detail view function 

def product_detail(request,id,slug):
    prod  = get_object_or_404(Product, id=id, slug=slug, available=True) 
    
    
    cart_product_form = CartAddProductForm()
    
    
    return render(request,'shop/detail.html',{'product':prod,'cart_product_form':cart_product_form})