from flask import json
from test_base import TestBase


class TestOrder(TestBase):
    """ Defines tests for the view methods of orders 
    """

    def setUp(self):
        self.create_valid_user()

    def test_accessing_user_orders_history_without_token(self):
        """ Tests a user accessing their order history without a token """
        response = self.client.get('/api/v2/users/orders')
        self.assertEqual(response.status_code, 401)

    def test_admin_accessing_all_user_orders_without_token(self):
        """ Tests Admin accessing all orders without a token """
        response = self.client.get('/api/v2/users/orders')
        self.assertEqual(response.status_code, 401)

    def test_admin_accessing_a_specific_order_without_token(self):
        """ Tests Admin accessing a specific order without a token """
        response = self.client.get('/api/v2/orders/<orderId>')
        self.assertEqual(response.status_code, 401)


    def test_accessing_orders_with_invalid_or_expired_token(self):
        """ Tests accessing the orders endpoint with an invalid
        or expired token """
        response = self.client.get('/api/v2/api/v2/users/orders',
                                   headers={'Authorization':
                                            'XBA5567SJ2K119'})
        self.assertEqual(response.status_code, 404)

    def test_posting_an_order_with_invalid_or_expired_token(self):
        """ Tests accessing the orders endpoint with an invalid
        or expired token """
        response = self.client.post('/api/v2/api/v2/users/orders',
                                   headers={'Authorization':
                                            'XBA5567SJ2K119'})
        self.assertEqual(response.status_code, 404)


    def test_create_an_order_for_non_menu_item(self):
        """ Tests placing an order with for non existant menu item """
        response = self.create_post_order()
        self.assertEqual(response.status_code, 200)
        self.assertIn('"message": "Item Not Found"', str(response.data))

    def test_create_order_with_blank_attributes(self):
        """ Tests creating a order with a blank item_name or quantity """
        order = {
            'item_name': '',
            'quantity': '',
        }
        response = self.client.post('/api/v2/users/orders',
                                    data=json.dumps(order),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        self.assertEqual(response.status_code, 406)

    def test_create_order_with_invalid_characters(self):
        """ Tests creating a menu with a blank item_name or quantity """
        menu = {
            'item_name': '@#$%',
            'quantity': '@#$%',
        }
        response = self.client.post('/api/v2/users/orders',
                                    data=json.dumps(menu),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        self.assertEqual(response.status_code, 406)

    def test_for_empty_keys(self):
        """ Tests creating a duplicate order(same attributes) """
        response = self.create_post_order_empty_keys()
        self.assertEqual(response.status_code, 406)
        self.assertIn('All keys are required',str(response.data))

        
    def test_get_all_orders(self):
        """ Tests fetching all menu """
        self.create_valid_order()
        response = self.client.get('/api/v2/orders/',
                                   headers={'Authorization':
                                            self.get_token()})
        self.assertEqual(response.status_code, 200)