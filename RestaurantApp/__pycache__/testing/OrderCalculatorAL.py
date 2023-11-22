import unittest
from order_calculator import AbstractOrderCalculator, OrderCalculatorAL, OrderCalculatorKS
from base_model import Menu, OrderItem, Order
from base_enums import OrderItemSize
class OrderCalculatorMock(AbstractOrderCalculator):

    def _get_vat_rate(self):
        return 0.12
    def _get_size_rate_amount(self, order_item_size):
        return 1.0

class AbstractOrderCalculatorTest(unittest.TestCase):
    
    def setUp(self):
        self.order_calculator_mock = OrderCalculatorMock()
        self.menu = Menu()

    def test_calculate_total_order_item_price(self):
    
    #STEP 1: Prepare the test objects (define test input)
        tiramisu = self.menu.get_menu_items().get(500)
        order_item = OrderItem(tiramisu, OrderItemSize.SMALL, 2)
    #STEP 2: Exectute method to be tested on  test objects
        total_order_item_price = self.order_calculator_mock.calculate_order_item_price(order_item)
    #STEP 3: Validate the test with the setUp method
        self.assertEqual(9.0, total_order_item_price)
        self.assertEqual(4.5, order_item.get_order_item_price())


    def test_calculate_total_order_item_amount(self):
        spring_rolls = self.menu.get_menu_items().get(201)
        vegeteraian_sushi = self.menu.get_menu_items().get(300)
        ramen = self.menu.get_menu_items().get(401)
        tiramisu = self.menu.get_menu_items().get(500)

        spring_rolls_order_item = OrderItem(spring_rolls, OrderItemSize.XXL,1)
        vegeteraian_sushi_order_item = OrderItem(vegeteraian_sushi, OrderItemSize.LARGE,2)
        ramen_order_item = OrderItem(ramen, OrderItemSize.MEDIUM,2)
        tiramisu_order_item = OrderItem(tiramisu, OrderItemSize.SMALL,2)

        order = Order()
        order.get_order_items().append(spring_rolls_order_item)
        order.get_order_items().append(vegeteraian_sushi_order_item)
        order.get_order_items().append(ramen_order_item)
        order.get_order_items().append(tiramisu_order_item)

        total_order_amount = self.order_calculator_mock.calculate_total_order_amount(order)

        self.assertEqual(35.5, total_order_amount)

    def test_calculate_total_order_amount_vat(self):
        total_order_amount_vat = self.order_calculator_mock.calculate_total_order_amount_vat(35.5)
        self.assertEqual(4.26, total_order_amount_vat)

#TVSH e shtetit Shqiptar check.

class OrderCalculatorALTest(unittest.TestCase):

    def setUp(self):
        self.order_calculator_al = OrderCalculatorAL()
    
    def test_get_vat_rate(self):
        vat_rate = self.order_calculator_al._get_vat_rate()
        self.assertEqual(0.2, vat_rate)
    
    def test_get_size_rate_amount(self):
        size_rate_amount_small = self.order_calculator_al._get_size_rate_amount(OrderItemSize.SMALL)
        self.assertEqual(0.9, size_rate_amount_small)

        size_rate_amount_medium = self.order_calculator_al._get_size_rate_amount(OrderItemSize.MEDIUM)
        self.assertEqual(1, size_rate_amount_medium)

        size_rate_amount_large = self.order_calculator_al._get_size_rate_amount(OrderItemSize.LARGE)
        self.assertEqual(1.25, size_rate_amount_large)

        size_rate_amount_xxl = self.order_calculator_al._get_size_rate_amount(OrderItemSize.XXL)
        self.assertEqual(1.3, size_rate_amount_xxl)

class OrderCalculatorKSTest(unittest.TestCase):

    def setUp(self):
        self.order_calculator_ks = OrderCalculatorKS()
    
    def test_get_vat_rate(self):
        vat_rate = self.order_calculator_ks._get_vat_rate()
        self.assertEqual(0.18, vat_rate)
    
    def test_get_size_rate_amount(self):
        size_rate_amount_small = self.order_calculator_ks._get_size_rate_amount(OrderItemSize.SMALL)
        self.assertEqual(0.7, size_rate_amount_small)

        size_rate_amount_medium = self.order_calculator_ks._get_size_rate_amount(OrderItemSize.MEDIUM)
        self.assertEqual(1, size_rate_amount_medium)

        size_rate_amount_large = self.order_calculator_ks._get_size_rate_amount(OrderItemSize.LARGE)
        self.assertEqual(1.2, size_rate_amount_large)

        size_rate_amount_xxl = self.order_calculator_ks._get_size_rate_amount(OrderItemSize.XXL)
        self.assertEqual(1.25, size_rate_amount_xxl)

if __name__ == '__main__':
    unittest.main()