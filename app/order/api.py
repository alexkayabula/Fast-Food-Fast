from flask.views import MethodView
from flask import Flask, jsonify, request, make_response, current_app as app
from app.order.order_model import Order
from app.menu.menu_model import Menu
from app.auth.auth_model import User
from app.auth.decorator import token_required
from app.order.order_helper import validate_order
from app.database.database import Database
from app.database.order_db_queries import OrderDbQueries
from app.database.menu_db_queries import MenuDbQueries



class OrderView(MethodView):
    decorators = [token_required]
    def post(self, current_user):
        """Place an order"""
        menu_db = MenuDbQueries()
        order_db = OrderDbQueries()
        data = request.get_json()
        if validate_order(data) != 'valid':
            return jsonify({'message': validate_order(data)}), 406

        elif validate_order(data) == 'valid':
            menu_query = menu_db.fetch_all_menu()
            for item in menu_query:
                if item['item_name'] == data['item_name']:
                    username =  current_user.username
                    order_db.insert_order_data(data, username)
                    response = {'message': 'You have placed an order successfully.'}
                    return make_response(jsonify(response)), 201
            return jsonify({'message': 'Item Not Found'})
        
    decorators = [token_required]
    def get(self, current_user):
        """User view their orders"""
        username = current_user.username
        orders = Order.get_orders(username)
        return orders
        
    
class OrderManage(MethodView):
    decorators = [token_required]
    def get(self, current_user, orderId):
        """Method for the Admin to view orders"""
        order_db = OrderDbQueries()
        if current_user.username == 'admin':
            if orderId:
                query = order_db.fetch_specific_order_by_parameter('orders', 'orderId', orderId)
                for order in query:
                   return jsonify({"orders" : order}), 200
                return jsonify({'msg': "order not found "}), 404
            all_orders = Order.get_all_orders()
            return all_orders
        return jsonify({'message' : "You do not have admin rights."})

    def put(self, current_user, orderId):
        """Method for the Admin to update an order"""
        order_db = OrderDbQueries()
        data = request.get_json()
        if current_user.username == 'admin':
            query = order_db.fetch_by_parameter('orders', 'orderId', orderId)
            if query:
                order_status = ['completed', 'cancelled', 'processing', 'New']
                status = data['status']
                if status in  order_status:
                    order_db.update_order_status(orderId, status)
                    updated_order = order_db.fetch_specific_order_by_parameter('orders', 'orderId', orderId)
                    return jsonify ({'message' : updated_order})
                return jsonify ({'message' : 'Invalid Status'})
            return jsonify ({'message' : "Order not Found"})
        return jsonify({'message' : "You do not have admin rights."})