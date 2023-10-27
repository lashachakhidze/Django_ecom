from django.contrib import admin
from .models import Product, Category, Cart, Favourite

# Register your models here.


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image', 'description')


# admin.site.register(Category, CategoryAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)
