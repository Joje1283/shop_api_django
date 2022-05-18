from django.contrib import admin
from .models import Order, Delivery, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["member", "delivery", "order_date"]


"""
Delivery
OrderItem
"""


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ["status", "city", "street", "zipcode"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "item", "order_price", "count"]
