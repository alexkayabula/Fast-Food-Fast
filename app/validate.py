"""This module contain functions that handle input validation"""
import re


def validate_user(data):
    """validates the user and return appropriate message"""
    try:
        if not data['name'].strip() or not data['username'].strip()\
                or not data['password'].strip():
            return "all fields are required"
        
        if not re.match("^[a-zA-Z]*$", data['name'].strip()):
            return "The name should only contain alphabatic characters"
        elif not re.match("^[a-zA-Z]*$", data['username'].strip()) or\
            not re.match("^[a-zA-Z0-9_]*$", data['password'].strip()):
            return "Inputs should only contain alphanemeric characters"
        else:
            return 'valid'
    except KeyError:
        return "All keys are required"


def validate_login(data):
    """validates the user and return an appropriate message"""
    try:
        if not data['username'].strip() or not data['password'].strip():
          return  "all fields are required"
        if not re.match("^[a-zA-Z0-9_ ]*$", data['username'].strip()) or\
            not re.match("^[a-zA-Z0-9_]*$", data['password'].strip()):
            return "Inputs should only contain alphanemeric characters"
        else:
            return 'valid'
    except KeyError:
        return "All keys are required"


def validate_order(data):
    """validates the order inputs and return appropriate message"""
    try:
        if not data['item_name'].strip()  or not data['quantity'].strip():
            return "all fields are required"
        if not re.match("^[a-zA-Z]*$", data['item_name'].strip()):
            return "order should only contain alphabetic characters "
        elif not re.match("^[0-9_]*$", data['quantity'].strip()):
            return "Quantity should be a number"
        else:
            return 'valid'
    except KeyError:
        return "All keys are required"


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