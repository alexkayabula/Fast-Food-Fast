from flask.views import MethodView
from flask import Flask, jsonify, request, make_response, current_app as app
from app.models import Menu, User, Order
from app.auth.decorator import token_required
from app.validate import validate_order
from app.database import Database, MenuDbQueries, OrderDbQueries, UserDbQueries


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
        return jsonify({'message': validate_order(data)}), 201
    
    decorators = [token_required]
    def get(self, current_user):
        order_db = OrderDbQueries()
        username = current_user.username
        orders = order_db.fetch_all_orders_by_parameter('orders', 'username', username)
        for order in orders:
            if order:
                return jsonify({'orders': orders}), 200
        return jsonify({'message' : 'You have not made any orders'})

    
class OrderManage(MethodView):
    decorators = [token_required]
    def get(self, current_user, order_id):
        """Method for the admin to view orders"""
        order_db = OrderDbQueries()
        if current_user.username == 'admin':
            if order_id:
                query = order_db.fetch_all_orders_by_parameter('orders', 'order_id', order_id)
                for order in query:
                   return jsonify({"orders" : order}), 200
                return jsonify({'msg': "order not found "}), 404
            else:
                orders = order_db.fetch_all_orders()
                if orders == []:
                    return jsonify(
                        {"message": " There are no orders orders at the moment."}), 200
                return jsonify({"orders" : orders}), 200
        return jsonify({'message' : "You do not have admin rights."})

    def put(self, current_user, order_id):
        """Method for the admin to update an order"""
        order_db = OrderDbQueries()
        if current_user.username == 'admin':
            if order_id:
                query = order_id.fetch_by_parameter('orders', 'order_id', order_id)
                order_db.update_order_status(order_id)
                return jsonify ({'message' : query})
            return jsonify ({'message' : "Order not Found"})
        return jsonify({'message' : "You do not have admin rights."})