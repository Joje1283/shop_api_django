from django.test import TestCase

from ..models import Item
from ..exceptions import NotEnoughStockException


class TestItem(TestCase):
    def setUp(self) -> None:
        Item.objects.create(
            name="정의란 무엇인가",
            price=15000,
            stock_quantity=100,
        )

    def test_재고_확인(self):
        book = Item.objects.first()
        self.assertEqual(book.stock_quantity, 100)

    def test_재고_추가(self):
        # given
        book = Item.objects.first()
        add_stock_quantity = 5

        # when
        current_stock_quantity = book.stock_quantity
        book.add_stock(add_stock_quantity)

        # then
        result_stock_quantity = current_stock_quantity + add_stock_quantity
        self.assertEqual(book.stock_quantity, result_stock_quantity)

    def test_재고_삭제(self):
        # geven
        book = Item.objects.first()
        remove_stock_quantity = 5

        # when
        current_stock_quantity = book.stock_quantity
        book.remove_stock(remove_stock_quantity)

        # then
        result_stock_quantity = current_stock_quantity - remove_stock_quantity
        self.assertEqual(book.stock_quantity, result_stock_quantity)

    def test_재고_삭제_예외(self):
        # geven
        book = Item.objects.first()
        remove_stock_quantity = 105

        # when
        try:
            book.remove_stock(remove_stock_quantity)
        except NotEnoughStockException as e:
            return

        # then
        self.fail("NotEnoughStockException 예외가 발생해야 한다.")
