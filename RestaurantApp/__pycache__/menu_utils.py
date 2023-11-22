from base_model import Drink, Meal, Menu
import csv
from costum_exception import InvalidMenuFile

class MenuPrinter():
    def print_menu(self, menu):
        menu_items = menu.get_menu_items()

        print("################### MENU #####################")

        for key in menu_items:
            menu_item = menu_items[key] 

            if (isinstance(menu_item, Meal)):
                description_text = " " if menu_item.get_description() == " " else " ( " + menu_item.get_description() + " ) "
                print (str(menu_item.get_product_id()) + " . " + str(menu_item.get_name()) + description_text + " | " + str(menu_item.get_price()) + " Euro")

            elif (isinstance(menu_item, Drink)):
                sugar_free_text = "Yes" if menu_item.get_sugar_free() else "No"
                print (str(menu_item.get_product_id()) + " . " + menu_item.get_name() + "(Sugar free: " + sugar_free_text + " ) | " + str(menu_item.get_price()) + " Euro")
            
        print("################### MENU #####################")

class MenuImporter:

    def import_menu(self, file_path):
       # imported_menu = Menu()

        menu_file = open(file_path)
        csv_reader = csv.reader(menu_file) 

        return self._transform_csv_menu_data_to_menu(csv_reader)
    
    def _transform_csv_menu_data_to_menu(self, csv_reader):
        imported_menu = Menu()
        for row in csv_reader: 
            product_id = int(row[0])
            product_name = row[1]
            product_price = float(row[2])
            product_category = row[3]

            if "meal" == product_category:
                product = Meal(product_id, product_name, product_price, "")
            elif "drink" == product_category:
                sugar_free = row[4]
                product = Drink(product_id, product_name, product_price, sugar_free)
            else:
                exception_message = "" .join("The menu file couldn't be processed as the product catogory from product ").join(product_name).join(" is invalid.")
                raise InvalidMenuFile(exception_message)
            
            imported_menu.get_menu_items().update({product_id: product})

        return imported_menu 
        