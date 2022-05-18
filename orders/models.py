from django.db import models

from members.models import Address


class Order(models.Model):
    member_id = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    delivery_id = models.OneToOneField("orders.Delivery", on_delete=models.CASCADE)
    order_date = models.DateTimeField(verbose_name="주문 시간", auto_now_add=True)

    class Status(models.TextChoices):
        ORDER = 'O'
        CANCEL = 'C'

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.ORDER)


class Delivery(Address):
    class Status(models.TextChoices):
        READY = 'R'
        COMP = 'C'

    status = models.CharField(verbose_name="배달 상태", max_length=2, choices=Status.choices, default=Status.READY)


class OrderItem(models.Model):
    order_id = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    item_id = models.ForeignKey("items.Item", on_delete=models.CASCADE)
    order_price = models.IntegerField(verbose_name="구매 가격")
    count = models.IntegerField(verbose_name="구매 수량")
