from django.contrib import admin
from .models.products import Product
from .models.category import Category
from .models.customer import Customer

from .models.productorder import ProductOrder

# Register your models here.
class productData(admin.ModelAdmin):
    list_display=("name", "price", "description", "image","category")
admin.site.register(Product,productData)    

class categoryData(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Category, categoryData)    

class customerData(admin.ModelAdmin):
    list_display=("name","mobile","email","password")
admin.site.register(Customer,customerData)

class productorderData(admin.ModelAdmin):
    list_display=("product","customer","quantity","price","address","mobile","date","status")
admin.site.register(ProductOrder,productorderData)    