from flask import jsonify, make_response
from app.database.database import Database
from app.database.menu_db_queries import MenuDbQueries


class Menu:
    '''  Defines a Menu class'''
    def __init__(self,item_name, price):
        ''' Initializes the order object'''
        self.item_name = item_name
        self.price = price
    
    def add_menu_item(self, data):
        menu_db = MenuDbQueries()
        menu_query = menu_db.fetch_all_menu()
        for menu_item in menu_query:
            if menu_item['item_name'] == data['item_name'] and \
                menu_item['price'] == data['price']:
                response = {'message': 'This food item already exists.'}
                return make_response(jsonify(response)), 409
        menu_db.insert_menu_data(data)
        response = {'message': 'You added a food item successfully.'}
        return make_response(jsonify(response)), 201
        
    @classmethod
    def get_all_menu(cls):
        menu_db = MenuDbQueries()
        menu = menu_db.fetch_all_menu()
        if menu == []:
            return jsonify(
                {"msg": " There is no menu item at the moment"}), 200
        return jsonify(menu), 200
      