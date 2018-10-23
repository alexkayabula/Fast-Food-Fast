"""This module contain functions that handle input validation"""
import re
def validate_menu(data):
    """validates the menu item and returns an appropriate message"""
    try:
        if not type(data['item_name']) == str or not type(data['price']) == str:
            return 'Invalid entry, Input should be in a valid json format'
        if not data['item_name'].strip() or not data['price'].strip():
            return  "All fields are required"
        if not re.match("^[a-zA-Z]*$", data['item_name'].strip()):
            return "The item name should only contain alphabetic characters"
        elif  not re.match("^[0-9]*$", data['price'].strip()):
            return "The price should only contain numeric characters"
        else:
            return 'valid'
    except KeyError:
        return "All keys are required"