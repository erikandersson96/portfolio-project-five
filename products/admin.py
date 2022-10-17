from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'watch_make',
        'price',
        'watch_size',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
