"""This module contain functions that handle input validation"""
import re
def validate_order(data):
    """validates the order inputs and return appropriate message"""
    try:
        if not type(data['item_name']) == str or not type(data['quantity']) == str:
            return 'Invalid entry, Input should be in a valid json format'
        if not data['item_name'].strip()  or not data['quantity'].strip():
            return "All fields are required"
        if not re.match("^[a-zA-Z]*$", data['item_name'].strip()):
            return "Item name should only contain alphabetic characters "
        elif not re.match("^[0-9_]*$", data['quantity'].strip()):
            return "Quantity should be an integer"
        else:
            return 'valid'
    except KeyError:
        return "All keys are required"
