class Restaurant:
    def __init__(self, name, address) -> None:
            
        self.__name = name
        self.__address = address
    
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    
    def set_address(self, address):
        self.__address = address
    def get_address(self):
        return self.__address

class Client:
    def __init__(self, name, phone_nr) -> None:
            
        self.__name = name
        self.__phone_nr = phone_nr
    
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    
    def set_phone_nr(self, phone_nr):
        self.__phone_nr = phone_nr
    def get_phone_nr(self):
        return self.__phone_nr

class Order:
    def __init__(self) -> None:

        self.__product_list = []
            
    def get_order_items(self):
        return self.__product_list
    
class Product:
    def __init__(self, product_id, name, price) -> None:
            
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    def set_product_id(self, product_id):
        self.__product_id = product_id
    def get_product_id(self):
        return self.__product_id

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    
    def set_price(self, price):
        self.__price = price
    def get_price(self):
        return self.__price

class Meal(Product):
    def __init__(self, product_id, name, price, description) -> None:
        super().__init__(product_id, name, price)

        self.__description = description

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description
        
class Drink(Product):
    def __init__(self, product_id, name, price, sugar_free) -> None:
        super().__init__(product_id, name, price)
        self.__sugar_free = sugar_free
    
    def set_sugar_free(self, sugar_free):
        self.__sugar_free = sugar_free
    def get_sugar_free(self):
        return self.__sugar_free

    
class Menu():

    def __init__(self) -> None:
        self.__menu_items = dict({})   
        self.__initialize_menu_products()

    def __initialize_menu_products(self):
        
        self.__menu_items.update({100: Meal(100, "Wakame Salad", 5.5, "Seaweed, Cucumber, Sesame Seeds")})
        self.__menu_items.update({101: Meal(101, "Summer Salad", 6.9, "Salmon, Green Salad, Arugula, Red Lola, Sunflower Seeds, Twitch Sause")})
        self.__menu_items.update({200: Meal(200, "Miso Soup", 4.8, "Tofu, Mushrooms, Susame Seeds, Onion, Soya Paste")})
        self.__menu_items.update({201: Meal(201, "Spring Rolls", 4.5, "Rice paper filled with vegetables and peppers sause.")})
        self.__menu_items.update({202: Meal(202, "Tempered Shrimps", 7.5, "Crispy shrimps, Spicy Mayo")})
        self.__menu_items.update({300: Meal(300, "Vegeteraian Sushi", 5.0, "Avocado, Cucumber, Onioon, Carrot, Pepper, Red Turnip")})
        self.__menu_items.update({301: Meal(301, "Smoked Salmon Sushi", 8.5, "Smoked Salmon, Avocado, Cheese Cream")})
        self.__menu_items.update({302: Meal(302, "Crab Sushi", 8.2, "Crab, Avocado, Cheese Cream")})
        self.__menu_items.update({400: Meal(400, "Chicken Noodles", 6.5, "Chicken Breast, Noodles, Carrot, Onion, Brocoli, Soya Sause, Corn, Sesame Seeds")})
        self.__menu_items.update({401: Meal(401, "Ramen", 6.0, "Chicken Breast, Noodles, Carrot, Onion, Brocoli, Boiled Egg, Ginger, Sesame Seeds")})
        self.__menu_items.update({450: Drink(450, "Water", 1.0, False)})
        self.__menu_items.update({451: Drink(451, "Coca cola", 2.0, True)})
        self.__menu_items.update({452: Drink(452, "Coca cola Zero", 2.0, False)})
        self.__menu_items.update({500: Meal(500, "Tiramisu", 4.5, "Espresso, Custard, Mascarpone Cheese, Vanilla, LadyFingers")})
        self.__menu_items.update({501: Meal(501, "Sweet Maki", 9.0, "Chocolate syrup, Banana, Avocado, Mango")})
    
    def get_menu_items(self):
        return self.__menu_items
    
class OrderItem:
    def __init__(self, product, order_item_size, quantity) -> None:
        self.__product = product
        self.__order_item_size = order_item_size
        self.__quantity = quantity 

        self.__order_item_price = 0.0
    
    def set_product(self, product):
        self.__product = product
    def get_product(self):
        return self.__product 
    
    def set_order_item_size(self, order_item_size):
        self.__order_item_size = order_item_size
    def get_order_item_size(self):
        return self.__order_item_size
    
    def set_quantity(self, quantity):
        self.__quantity = quantity 
    def get_quantity(self):
        return self.__quantity 
    
    def get_order_item_price(self):
        return self.__order_item_price
    def set_order_item_price(self, order_item_price):
        self.__order_item_price = order_item_price