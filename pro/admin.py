from django.contrib import admin

from .models import items,products,cart,buyed
admin.site.register(items)
admin.site.register(products)
admin.site.register(cart)
admin.site.register(buyed)