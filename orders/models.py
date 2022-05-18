from django.db import models

from members.models import Address


class Order(models.Model):
    member = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    delivery = models.OneToOneField("orders.Delivery", on_delete=models.CASCADE)
    order_date = models.DateTimeField(verbose_name="주문 시간", auto_now_add=True)

    class Status(models.TextChoices):
        ORDER = 'O', '주문됨'
        CANCEL = 'C', '취소됨'

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.ORDER)

    def __str__(self):
        # status의 값이 아닌 display name을 반환
        return f"주문 정보({self.member}님에 의해 {[choice[1] for choice in self.Status.choices if choice[0] == self.status][0]})"


class Delivery(Address):
    class Status(models.TextChoices):
        READY = 'R', '배송 준비'
        COMP = 'C', '배송 완료'

    status = models.CharField(verbose_name="배송 상태", max_length=2, choices=Status.choices, default=Status.READY)

    def __str__(self):
        # status의 값이 아닌 display name을 반환
        return [choice[1] for choice in self.Status.choices if choice[0] == self.status][0]


class OrderItem(models.Model):
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    item = models.ForeignKey("items.Item", on_delete=models.CASCADE)
    order_price = models.IntegerField(verbose_name="구매 가격")
    count = models.IntegerField(verbose_name="구매 수량")

    def __str__(self):
        return f"{self.item.name} - {self.order.status}"

