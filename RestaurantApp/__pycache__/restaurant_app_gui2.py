from kivymd.app import MDApp
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from kivy.core.window import Window
from menu_utils import MenuImporter
from base_model import Restaurant, Client, Order, Product
from base_enums import OrderItemSize
from order_utils import OrderManager, InvoicePrinter
from order_calculator import OrderCalculatorAL, OrderCalculatorKS


class RestorantApp(MDApp):

    __selected_product = None

    def build(self):
        Window.size = (1000, 800)
        self.screen = Builder.load_file("restaurant_app_gui2.kv")

        # define varables for UI element values 
        #first_box_layout = self.screen.ids.first_box_layout
        #second_box_layout = self.screen.ids.second_box_layout
        #third_box_layout = self.screen.ids.third_box_layout
        self.quantity_input = self.screen.ids.quantity_input
        self.order_item_size_spinner = self.screen.ids.spinner
        self.check_box_al = self.screen.ids.check_box_al
        self.check_box_ks = self.screen.ids.check_box_ks
        self.name_field = self.screen.ids.name_textfield
        self.phone_number_textfield = self.screen.ids.phone_nr_textfield
        self.invoice_label = self.screen.ids.invoice_label


        menu_importer = MenuImporter()
        menu = menu_importer.import_menu("menu-list.csv")
        product_list = list(menu.get_menu_items().values())
        table_row_data = []

        for product in product_list:
            table_row_data.append((product.get_product_id(), product.get_name(), product.get_price()))
        
        menu_table = MDDataTable(
            size_hint=(1, 1),
            check = True,
            rows_num = 10,
            column_data = [
                ("Id", dp(20)),
                ("Name", dp(25)),
                ("Price", dp(30)),

            ],
            row_data = table_row_data
        )
        content_boxLayout = self.screen.ids.first_box_layout
        content_boxLayout.add_widget(menu_table)
        menu_table.bind(on_row_press=self.on_row_press)

        self.order_table = MDDataTable(
            size_hint=(1, 1),
            check = True,
            rows_num = 10,
            padding = [0, 25, 0, 0],
            column_data = [
                ("Id", dp(20)),
                ("Name", dp(25)),
                ("Price", dp(20)),
                ("Quantity", dp(20)),
                ("Size", dp(20))
            ],
            row_data = []
        )
        content_boxLayout2 = self.screen.ids.second_box_layout
        content_boxLayout2.add_widget(self.order_table)


        return self.screen
    def add_product_to_order(self, instance):
        if self.__selected_product is None:
            ##############TODO create message pop up to warn user
            return
        
        quantity = self.quantity_input.text
        order_item_size = self.order_item_size_spinner.text

        if quantity and order_item_size:
            product_data = [
                self.__selected_product[0],
                self.__selected_product[1],
                self.__selected_product[2],
                quantity,
                order_item_size
            ]
            
            self.order_table.row_data.append(product_data)

        self.__selected_product = None
        self.quantity_input.text = ""
        self.order_item_size_spinner.text = "Select Size"

    def calculate_amount(self, instance):
        restaurant = Restaurant("Twitch", "Route 214")
        name = self.name_field.text
        phone_nr = self.phone_number_textfield.text

        client = Client(name, phone_nr)

        order_calculator = OrderCalculatorAL() if self.check_box_al.active else OrderCalculatorKS()

        order = Order()
        order_manager = OrderManager()

        for product in self.order_table.row_data:
            product_id = int(product[0])
            product_name = str(product[1])
            price = float(product[2])
            quantity = float(product[3])
            order_item_size = self._get_order_item_size_as_enum(str(product[4]))
            ordered_product = Product(product_id, product_name, price)
            order_manager.add_order_item(order, ordered_product, quantity, order_item_size)
        
        order_amount = order_calculator.calculate_order_amount(order)

        invoice_printer = InvoicePrinter()
        invoice = invoice_printer.get_invoice(restaurant, client, order, order_amount, order_calculator.get_vat_rate(False))
        self.invoice_label.text = invoice


    def on_row_press(self, instance_table, instance_row):
        row_number = int(instance_row.index/len(instance_table.column_data))
        self.__selected_product = instance_table.row_data[row_number]

    def _get_order_item_size_as_enum(self, order_item_size_as_string):
        match order_item_size_as_string:
            case "Small":
                return OrderItemSize.SMALL
            case "Medium":
                return OrderItemSize.MEDIUM
            case "Large":
                return OrderItemSize.LARGE
            case "XXL":
                return OrderItemSize.XXL
            case _:
                print("No Valid order item size: " + order_item_size_as_string)
                return 1
    
RestorantApp().run()