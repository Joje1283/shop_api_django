from django.urls import path
from .views import order_create_view, OrderListView, order_cancel_view

urlpatterns = [
    path("new/", order_create_view, name="order_create_view"),
    path("", OrderListView.as_view(), name="order_list_view"),
    path("<int:order_id>/cancel", order_cancel_view, name="order_cancel_view")
]