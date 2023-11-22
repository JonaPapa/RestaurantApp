from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.lang import Builder
from menu_utils import MenuImporter

class RestaurantAppGUI(MDApp):

    __selected_product = None
    
    def build(self):
        Window.size = (900, 700)
        self.screen = Builder.load_file('restaurant_app_gui.kv') 

        
        menu_import = MenuImporter()
        menu = menu_import.import_menu('menu-list.csv')
        product_list = list(menu.get_menu_items().values())

        table_row_data = []
        for product in product_list:
           table_row_data.append((product.get_product_id(), product.get_name(), product.get_price()))

        menu_table = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.5),
            check = True,
            rows_num = 10,
            column_data = [
                ("Id", dp(30)),
                ("Name", dp(50)),
                ("Price", dp(30))
            ],
            row_data = table_row_data
        )
        menu_table.bind(on_check_press=self.checked)

        menu_table.bind(on_row_press=self.on_row_press)

        self.order_table = MDDataTable(
            size_hint = (1, 1),
            padding = [0,33,0,0],
            check = True,
            rows_num = 10,
            column_data = [
                ("Id", dp(30)),
                ("Name", dp(50)),
                ("Price", dp(30)),
                ("Quantity", dp(20)),
                ("Order Item Size", dp(40))
            ],

            row_data = []
        )

        self.order_table.bind(on_row_press=self.on_row_press)

        return self.screen
    
    def checked(self, instance_table, current_row):
        print(current_row)
    
    def on_row_press(self, instance_table, instance_row):
        row_number = int(instance_row.index/len(instance_table.column_data))
        self.__selected_product = instance_table.row_data[row_number]

        #self.get_text_fields_box_layout().children[2].text = str(self.__selected_product[0])
        #self.get_text_fields_box_layout().children[1].text = str(self.__selected_product[1])
        #self.get_text_fields_box_layout().children[0].text = str(self.__selected_product[2])

    
    def add_row(self):
        id = self.get_text_fields_box_layout().children[2].text
        name = self.get_text_fields_box_layout().children[1].text
        price = self.get_text_fields_box_layout().children[0].text
        self.get_menu_datatable_widget().row_data.append([id, name, price])

    def update_row(self):
        id = int(self.get_text_fields_box_layout().children[2].text)
        name = self.get_text_fields_box_layout().children[1].text
        price = float(self.get_text_fields_box_layout().children[0].text)
        update_row_data = (id, name, price)

        row_data = self.get_menu_datatable_widget().row_data
        index = self.get_menu_datatable_widget().row_data_index(self.__selected_product)
        row_data[index] = update_row_data

    def delete_row(self):
        table_data = self.get_menu_datatable_widget().row_data
        table_data.remove(self.__selected_product)

    def get_text_fields_box_layout(self):
        #root ---> kivy - python
        md_card = self.root.children[0]
        general_box_layout = md_card.children[1]
        text_field_box_layout = general_box_layout.children[1]
        return text_field_box_layout
    
    def add_menu_datatable_widget(self):
        md_card = self.root.children[0]
        menu_table = md_card.children[0]
        return menu_table
    
    
RestaurantAppGUI().run()
