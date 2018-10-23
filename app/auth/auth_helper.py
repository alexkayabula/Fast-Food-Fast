"""This module contain functions that handle input validation"""
import re


def validate_user(data):
    """validates the user and return appropriate message"""
    try:
        if not type(data['name']) == str or not type(data['username']) == str or not type(data['password']) == str :
            return 'Invalid entry, Input should be in a valid json format'
        if not data['name'].strip() or not data['username'].strip()\
                or not data['password'].strip():
            return "All fields are required"
        
        if not re.match("^[a-zA-Z]*$", data['name'].strip()):
            return "The name should only contain alphabetic characters"
        if not re.match("^[a-zA-Z]*$", data['username'].strip()):
            return "The username should only contain alphabetic characters"
        elif not re.match("^[a-zA-Z0-9_]*$", data['password'].strip()):
            return "The password should only contain alphanumeric characters"
        else:
            return 'valid'
    except KeyError:
        return "All keys are required"


def validate_login(data):
    """validates the user and return an appropriate message"""
    try:
        if not type(data['username']) == str or not type(data['password']) == str:
            return 'Invalid entry, Input should be in a valid json format'
        if not data['username'].strip() or not data['password'].strip():
          return  "All fields are required"
        if not re.match("^[a-zA-Z]*$", data['username'].strip()):
            return "The username should only contain alphabetic characters"
        elif not re.match("^[a-zA-Z0-9_]*$", data['password'].strip()):
            return "The password should only contain alphanumeric characters"
        else:
            return 'valid'
    except KeyError:
        return "All keys are required"
