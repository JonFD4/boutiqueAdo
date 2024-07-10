from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display=(
        'sku', 'name', 'category','price', 'rating',
        'image'
    )

    # sort the products by sku. Although it is one field, it is possible to sort on multiple columns. Hence, it is in a tuple. Reverse by add a 'minus' at the end.
    ordering=('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display=(
        'friendly_name',
        'name'
    )
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)