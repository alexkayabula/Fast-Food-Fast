"""This module contains classes order and its method"""
import uuid
food_orders = []


class Order:
    def __init__(self, order_id, item_name, price, order_date, user_name,
                 status):
        pass

    @classmethod
    def existing_order(cls, item_name, price, order_date, user_name):
        """A method to check if the same order already exists """
        for order in food_orders:
            if order['item_name'] == item_name and order['price'] == \
                    price and order['order_date'] == order_date and \
                    order['user_name'] == user_name:
                return True
        return False

    @classmethod
    def make_order(cls, item_name, price, order_date, user_name):
        """A method for making a order"""
        cls.data = {}
        if cls.existing_order(item_name, price, order_date, user_name):
            return "Order Already Exists"
        else:
            cls.data['order_id'] = uuid.uuid1()
            cls.data['item_name'] = item_name
            cls.data['price'] = price
            cls.data["order_date"] = order_date
            cls.data["status"] = 'Pending'
            cls.data["user_name"] = user_name
            food_orders.append(cls.data)
            return "Order Made Successfully"

    @classmethod
    def get_all_orders(cls):
        """ Return all the food_orders"""
        return food_orders
