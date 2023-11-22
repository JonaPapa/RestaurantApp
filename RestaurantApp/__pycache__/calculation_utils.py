from base_enums import Location
import order_calculator 

class OrderCalculatorFactory:

    @staticmethod
    def get_order_calculator_by_location(location):
        match(location):
            case Location.ALBANIA:
                return order_calculator.OrderCalculatorAL()
            case Location.KOSOVA:
                return order_calculator.OrderCalculatorKS()
            case _:
                raise Exception("Current Location is invalid. OrderCalculator could not be determinded.")

