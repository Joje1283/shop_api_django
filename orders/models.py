from django.db import models, transaction

from items.exceptions import NotEnoughStockException
from members.models import Address, Member
from items.models import Item


class OrderManager(models.Manager):
    @transaction.atomic
    def order_create(self, member_id: int, item_id: int, count: int) -> int:
        """
        비즈니스 로직 (관심사의 분리는 제외하였다)
        또는 애플리케이션 로직
        """
        # 엔티티 조회
        member: Member = Member.objects.get(pk=member_id)
        item: Item = Item.objects.get(pk=item_id)

        # 배송정보 생성
        delivery: Delivery = Delivery.objects.create(**member.address)

        # 주문 생성
        order = self.create(member=member, delivery=delivery)

        # 주문 상품 생성
        OrderItem.objects.create(order=order, item=item, order_price=item.price, count=count)
        return order.pk


class Order(models.Model):
    member = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    delivery = models.OneToOneField("orders.Delivery", on_delete=models.CASCADE)
    order_date = models.DateTimeField(verbose_name="주문 시간", auto_now_add=True)

    class Meta:
        ordering = ["pk"]

    class Status(models.TextChoices):
        ORDER = 'O', '주문됨'
        CANCEL = 'C', '취소됨'

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.ORDER)

    objects = OrderManager()

    def __str__(self):
        # status의 값이 아닌 display name을 반환
        return f"주문 정보({self.member}님에 의해 {[choice[1] for choice in self.Status.choices if choice[0] == self.status][0]})"

    @property
    def status_str(self):
        return [choice[1] for choice in self.Status.choices if choice[0] == self.status][0]

    @property
    def first_order_item(self):
        return self.orderitem_set.first()

    """
    비즈니스 로직
    """
    def cancel(self):
        if self.delivery.status == Delivery.Status.COMP:
            raise NotEnoughStockException("이미 배송된 상품은 취소가 불가능합니다.")
        self.status = self.Status.CANCEL[0]
        self.save()
        for order_item in self.orderitem_set.all():
            order_item.cancel()

    """
    조회 로직
    """

    @property
    def total_price(self):
        # Todo: 쿼리 개선 검토
        return sum(order_item.total_price for order_item in self.orderitem_set.all())


class Delivery(Address):
    class Status(models.TextChoices):
        READY = 'R', '배송 준비'
        COMP = 'C', '배송 완료'

    status = models.CharField(verbose_name="배송 상태", max_length=2, choices=Status.choices, default=Status.READY)

    def __str__(self):
        # status의 값이 아닌 display name을 반환
        return [choice[1] for choice in self.Status.choices if choice[0] == self.status][0]


class OrderItemManager(models.Manager):
    def create(self, item, count, **kwargs):
        item.remove_stock(count)
        return super().create(item=item, count=count, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    item = models.ForeignKey("items.Item", on_delete=models.CASCADE)
    order_price = models.IntegerField(verbose_name="구매 가격")
    count = models.IntegerField(verbose_name="구매 수량")

    objects = OrderItemManager()

    def __str__(self):
        return f"{self.item.name} - {self.order.status}"

    """
    비즈니스 로직
    """
    def cancel(self):
        self.item.add_stock(self.count)

    """
    조회 로직
    """
    @property
    def total_price(self):
        return self.order_price * self.count
