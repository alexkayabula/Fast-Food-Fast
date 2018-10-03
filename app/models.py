"""This module handles database queries"""


class User:

    def __init__(self, user_id, name, username, password, admin_status):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.password = password
        self.admin_status = admin_status


class Order:
    '''  Defines a Order class'''
    def __init__(self, order_id, item_name, quantity, username, status):
        ''' Initializes the order object'''
        self.order_id = order_id
        self.item_name = item_name
        self.quantity = quantity
        self.username = username
        self.status = status

class Menu:
    '''  Defines a Menu class'''
    def __init__(self, item_id, item_name, price):
        ''' Initializes the order object'''
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
