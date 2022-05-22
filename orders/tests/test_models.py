from django.test import TestCase

from items.exceptions import NotEnoughStockException
from orders.models import OrderManager, Order, Delivery, OrderItemManager, OrderItem
from members.models import Member
from items.models import Item


class TestOrderManager(TestCase):
    def setUp(self) -> None:
        self.member_id = Member.objects.join(
            username="paul",
            password="1234",
            first_name="jaesik",
            last_name="cho",
            email="paul@test.com",
        )
        self.item = Item.objects.create(
            name="정의란 무엇인가",
            price=15000,
            stock_quantity=100,
        )
        print('deb')

    def test_주문_생성(self):
        # 주문 생성 전 상태 확인
        self.assertFalse(Delivery.objects.exists())
        self.assertFalse(OrderItem.objects.exists())
        item = Item.objects.get(pk=self.item.pk)
        self.assertEqual(item.stock_quantity, 100, "재고 확인")

        # 주문 생성하기
        order_count = 5
        order_id = Order.objects.order_create(member_id=self.member_id, item_id=self.item.pk, count=order_count)
        order = Order.objects.get(pk=order_id)

        # 주문 생성 후 상태 확인
        self.assertEqual(self.member_id, order.member.pk)
        self.assertTrue(Delivery.objects.exists())
        self.assertTrue(OrderItem.objects.exists())

        self.assertEqual(order.status, Order.Status.ORDER[0], "상품 주문시 상태는 ORDER")
        self.assertEqual(15000*order_count, order.total_price, "주문 가격은 가격*수량")

        item = Item.objects.get(pk=self.item.pk)
        self.assertEqual(item.stock_quantity, 95, "재고 확인")

    def test_주문_재고수량초과(self):
        # 주문 생성하기
        try:
            order_count = 105
            Order.objects.order_create(member_id=self.member_id, item_id=self.item.pk, count=order_count)
        except NotEnoughStockException:
            return
        self.fail("재고 수량 부족 예외가 발생해야 한다.")

    def test_주문_취소(self):
        # given
        # 주문 생성하기
        order_count = 5
        order_id = Order.objects.order_create(member_id=self.member_id, item_id=self.item.pk, count=order_count)
        order = Order.objects.get(pk=order_id)

        # when
        order.cancel()

        # then
        result_order = Order.objects.get(pk=order_id)
        self.assertEqual(Order.Status.CANCEL[0], result_order.status, "주문 취소시 상태는 CANCEL이다.")
        item = Item.objects.get(pk=self.item.pk)
        self.assertEqual(100, item.stock_quantity, "주문이 취소된 상품은 그만큼 재고가 증가해야 한다.")



