from flask.views import MethodView
from flask import Flask, jsonify, request, make_response, current_app as app
from app.menu.menu_model import Menu
from app.auth.decorator import token_required
from app.menu.menu_helper import validate_menu
from app.database.database import Database
from app.database.menu_db_queries import MenuDbQueries


class MenuView(MethodView):
    decorators = [token_required]
    def post(self, current_user):
        """Add a new food item"""
        menu_db = MenuDbQueries()
        data = request.get_json()
        if current_user.username == 'admin':
            if validate_menu(data) != 'valid':
                return jsonify({'message': validate_menu(data)}), 406

            elif validate_menu(data) == 'valid':
                menu_query = menu_db.fetch_all_menu()
                for menu_item in menu_query:
                    if menu_item['item_name'] == data['item_name'] and \
                        menu_item['price'] == data['price']:
                        response = {
                            'message': 'This food item already exists.',
                        }
                        return make_response(jsonify(response)), 409
                menu_db.insert_menu_data(data)
                response = {'message': 'You added a food item successfully.'}
                return make_response(jsonify(response)), 201
            return jsonify({'message': validate_menu(data)}), 201
        return jsonify({'message' : "You do not have admin rights"})
    
    decorators = [token_required]
    def get(self, current_user):
        menu_db = MenuDbQueries()
        menu = menu_db.fetch_all_menu()
        if current_user.username == 'admin':
            if menu == []:
               return jsonify(
                    {"msg": " There is no menu item at the moment"}), 200
            return jsonify(menu), 200
        return jsonify({'message' : "You do not have admin rights"})