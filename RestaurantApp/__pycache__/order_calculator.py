from abc import ABC, abstractmethod
from base_enums import OrderItemSize
from costum_exception import InvalidOrderItemSize
class AbstractOrderCalculator(ABC):
    def calculate_total_order_amount(self, order) -> float:

        order_items = order.get_order_items()
        total_order_amount = 0.0
        
        for order_item in order_items:
            total_order_amount += self.calculate_order_item_price(order_item) 

        return total_order_amount

    def calculate_total_order_amount_vat(self, total_order_amount):
        return total_order_amount * self._get_vat_rate()
    
    def calculate_order_amount (self, order):
        total_order_amount = self.calculate_total_order_amount(order)
        total_order_amount_vat = self.calculate_total_order_amount_vat(total_order_amount)
        total_order_amount_with_vat = total_order_amount + total_order_amount_vat

        order_amount = OrderAmount(total_order_amount, total_order_amount_vat, total_order_amount_with_vat)

        return order_amount


    def calculate_order_item_price (self, order_item):
        size_rate_amount = self._get_size_rate_amount(order_item.get_order_item_size())
        product = order_item.get_product()
        total_order_item_price_single = product.get_price() * size_rate_amount
        order_item.set_order_item_price(total_order_item_price_single)
        if (order_item.get_quantity() == 0):
            raise Exception("Invalid order item quantity!")
        
        return total_order_item_price_single * order_item.get_quantity() 
    
    def get_vat_rate(self, decimal):
        if decimal == True:
            return self._get_vat_rate()
        else:
            return self._get_vat_rate() * 100

    @abstractmethod
    def _get_vat_rate(self):
        pass
    
    @abstractmethod
    def _get_size_rate_amount(self, order_item_size):
        pass
          
class OrderAmount():
    def __init__(self, total_order_amount, total_order_amount_vat, total_order_amount_with_vat) -> None:

        self.__total_order_amount = total_order_amount
        self.__total_order_amount_vat = total_order_amount_vat
        self.__total_order_amount_with_vat = total_order_amount_with_vat
    
    def set_total_order_amount(self, total_order_amount):
        self.__total_order_amount = total_order_amount
    def get_total_order_amount(self):
        return self.__total_order_amount
    
    def set_total_order_amount_vat(self, total_order_amount_vat):
        self.__total_order_amount_vat = total_order_amount_vat
    def get_total_order_amount_vat(self):
        return self.__total_order_amount_vat
    
    def set_total_order_amount_with_vat(self, total_order_amount_with_vat):
        self.__total_order_amount_with_vat = total_order_amount_with_vat
    def get_total_order_amount_with_vat(self):
        return self.__total_order_amount_with_vat
    
class OrderCalculatorAL(AbstractOrderCalculator):
    
    def __init__(self) -> None:
        self.__VAT_RATE = 0.2
        
    def _get_vat_rate(self):
        return self.__VAT_RATE
    
    def _get_size_rate_amount(self, order_item_size):
        match order_item_size:
            case OrderItemSize.SMALL:
                return 0.9
            case OrderItemSize.MEDIUM:
                return 1
            case OrderItemSize.LARGE:
                return 1.25
            case OrderItemSize.XXL:
                return 1.3
            case _:
                raise InvalidOrderItemSize("No valid order item size: " + order_item_size)
                     
            
class OrderCalculatorKS(AbstractOrderCalculator):

    __VAT_RATE = 0.18
    
    def _get_vat_rate(self):
        return self.__VAT_RATE
    
    def _get_size_rate_amount(self, order_item_size):
        match order_item_size:
            case OrderItemSize.SMALL:
                return 0.7
            case OrderItemSize.MEDIUM:
                return 1
            case OrderItemSize.LARGE:
                return 1.2
            case OrderItemSize.XXL:
                return 1.25
            case _:
                raise InvalidOrderItemSize("No valid order item size: " + order_item_size)