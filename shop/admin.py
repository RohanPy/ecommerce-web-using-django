from django.contrib import admin
from .models import Category, Product

# Register your models here.


# registering category model to the admin site 
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
    
    
    
    
    
    

# registering product model to the admin site 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','available','created','updated']
    
    list_filter = ['available','created','updated']
    
    list_editable = ['price','available']    
    
    prepopulated_fields = {'slug':('name',)}