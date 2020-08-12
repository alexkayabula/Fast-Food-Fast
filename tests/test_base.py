import unittest
import psycopg2
from flask import json
from app import create_app
from app.database.database import Database


class TestBase(unittest.TestCase):
    """ Base class for all test classess """
    app = create_app('TESTING')
    app.app_context().push()
    client = app.test_client()

    user = {
        'name': ' joel',
        'username': 'joel',
        'password': 'password'
    }

    valid_user = {
        'name': 'admin',
        'username': 'admin',
        'password': 'admin'
    }

    valid_menu_item = {
        'item_name': 'fish',
        'price': "3000",
    }

    invalid_order = {
            'item_name': '@#$%',
            'quantity': '@#$%',
        }

    valid_order_item = {
        'item_name': 'fish',
        'quantity': '3',
    }
    
    valid_update = {
        'status' : 'completed'
    }

    invalid_update = {
        'status' : ''
    }

    order_invalid_quantity = {
            'item_name': 'fish',
            'quantity': '@#',
        }

    order_empty_key ={
        '' : 'fish',
        'quantity' : '5'
    }

    def setUp(self):
        """Example"""
        """db = Database('postgresql://YOUR_DATABASE_USERNAME:YOUR_DATABASE_PASSWORD@localhost:5432/YOUR_DATABASE_NAME')"""
        db = Database('postgresql://postgres:k0779211758aj@localhost:5432/order_db')
        db.create_tables()
        self.create_valid_user()

    def create_valid_user(self):
        """ Registers a user to be used for tests"""
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps(self.valid_user),
                                    content_type='application/json')
        return response

    def get_token(self):
        ''' Generates a token to be used for tests'''
        response = self.client.post('/api/v2/auth/login',
                                    data=json.dumps(self.valid_user),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        return data['token']

    def create_valid_menu(self):
        """ Creates a valid menu to be used for tests """
        response = self.client.post('api/v2/menu',
                                    data=json.dumps(self.valid_menu_item),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        return response
    def create_valid_order(self):
        """ Creates a valid order to be used for tests """
        response = self.client.post('api/v2/users/orders',
                                    data=json.dumps(self.valid_order_item),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        return response
         
    def update_an_order(self):
        """ Testing updating an order """
        response = self.client.put('api/v2/orders/<int:orderId>',
                                    data=json.dumps(self.valid_update),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        return response

    def tearDown(self):
        db = Database(
            'postgresql://admin:password@localhost:5432/test_db')
        db.trancate_table("users")
        db.trancate_table("orders")
        db.trancate_table("menu")