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
        data = request.get_json()
        if current_user.username == 'admin':
            if validate_menu(data) != 'valid':
                return jsonify({'message': validate_menu(data)}), 406
            elif validate_menu(data) == 'valid':
                #the trick
                menu = Menu(data['item_name'], data['price'])
                return menu.add_menu_item(data)
            return jsonify({'message': validate_menu(data)}), 201
        return jsonify({'message' : "You do not have admin rights"})
    
    decorators = [token_required]
    """Get all food items"""
    def get(self, current_user):
        menu = Menu.get_all_menu()
        return menu