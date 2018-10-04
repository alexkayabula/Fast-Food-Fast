"""This module contain functions that handle input validation"""
import re
def validate_menu(data):
    """validates the menu item and returns an appropriate message"""
    try:
        if not data['item_name'].strip() or not data['price'].strip():
            return  "all fields are required"
        if not re.match("^[a-zA-Z]*$", data['item_name'].strip()):
            return "Input should contain alphabetic characters only"
        elif  not re.match("^[0-9]*$", data['price'].strip()):
            return "Inputs should only contain numeric characters only"
        else:
            return 'valid'
    except KeyError:
        return "All keys are required"