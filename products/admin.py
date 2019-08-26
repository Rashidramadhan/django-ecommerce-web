from django.contrib import admin

# Register your models here.
from .models import Product, Order, User, Brand, Order_product, Payment, Order_history, Stock_level, Delivery_option, Product_type

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(Brand)
admin.site.register(Order_product)
admin.site.register(Payment)
admin.site.register(Order_history)
admin.site.register(Stock_level)
admin.site.register(Delivery_option)
admin.site.register(Product_type)

