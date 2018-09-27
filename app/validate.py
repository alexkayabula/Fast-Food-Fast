"""This module contain functions that handle input validation"""
from datetime import datetime
import re


def validate_order(data):
    '''validates the order and return appropriate message'''
    try:
        if not data['item_name'].strip() or not data['price'].strip()\
                                         or not data['user_name'].strip()\
                                         or not data['order_date'].strip():
            return "All fields are required"

        elif not re.match("^[a-zA-Z]*$", data['item_name'].strip()):
            return "Item name should only contain alphabetic characters"
        elif not re.match("^[a-zA-Z]*$", data['user_name'].strip()):
            return "Username should only contain alphabetic characters"
        elif not re.match("^[0-9]*$", data['price'].strip()):
            return "Price should only contain Numeric characters"
        else:
            return 'valid'
    except KeyError:
        return "All keys are required"


def validate_date(order_date):
    '''check that the order date'''
    try:
        order_date = datetime.strptime(order_date, '%Y-%m-%d')
    except ValueError:
        return "Incorrect date, should be YYYY-MM-DD"
    if order_date < datetime.now():
        return "Order cannot have a past date"
    return 'valid'
