import uuid
from flask.views import MethodView
from flask import jsonify, request, make_response
from app.models import Order
from app.validate import validate_date, validate_order


class OrderAPI(MethodView):
     
    @classmethod
    def get(cls, order_id):
        try:
            if order_id:
                order_id = uuid.UUID(order_id)
                orders = Order.get_all_orders()
                for order in orders:   
                    if order_id == order['order_id']:
                        return jsonify(order), 200
                return jsonify({'message': "Order Not Found "}), 404
            else:
                orders = Order.get_all_orders()
                if orders == []:
                    response = {"Orders": orders}
                    return make_response(jsonify(response)), 200
                return jsonify({"Orders": orders}), 200
        except ValueError:
            return jsonify("Invalid order_id, Server Error"), 500
    
    @classmethod
    def post(cls):
        data = request.json
        item_name = data["item_name"]
        price = data["price"]
        order_date = data["order_date"]
        user_name = data["user_name"]
        if validate_date(data['order_date']) != 'valid':
                return jsonify({'message': validate_date
                               (data['order_date'])}), 406
        elif validate_order(data) == 'valid':
            new_order = Order.make_order(item_name, price, order_date,
                                         user_name)
            if new_order == "Order Made Successfully":
                return jsonify({'message': new_order}), 201
            return jsonify({'message': new_order}), 409
        return jsonify({'message': validate_order(data)}), 406
    
    @classmethod
    def put(cls, order_id):
        try:
            if order_id:
                order_id = uuid.UUID(order_id)
                orders = Order.get_all_orders()
                for order in orders:
                    if order_id == order['order_id']:
                        order['status'] = 'Completed'
                        return jsonify({'message': "Order Completed"}), 200
                return jsonify({'message': "Order Not Found "}), 404
        except ValueError:
            return jsonify("Invalid order_id, Server Error"), 500