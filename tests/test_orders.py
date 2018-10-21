from flask import json
from test_base import TestBase


class TestOrder(TestBase):
    """ Defines tests for the view methods of orders 
    """
    def test_accessing_user_orders_history_without_token(self):
        """ Tests a user accessing their order history without a token """
        response = self.client.get('/api/v2/users/orders')
        self.assertEqual(response.status_code, 401)
        self.assertIn('Token is missing', str(response.data))

    def test_admin_accessing_all_user_orders_without_token(self):
        """ Tests Admin accessing all orders without a token """
        response = self.client.get('/api/v2/users/orders')
        self.assertEqual(response.status_code, 401)
        self.assertIn('Token is missing', str(response.data))

    def test_posting_order_with_empty_keys(self):
        """ Creates an order with empty keys """
        response = self.client.post('api/v2/users/orders',
                                    data=json.dumps(self.order_empty_key),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        self.assertEqual(response.status_code, 406)
        self.assertIn('All keys are required', str(response.data))


    def test_admin_accessing_a_specific_order_without_token(self):
        """ Tests Admin accessing a specific order without a token """
        response = self.client.get('/api/v2/orders/<int:orderId>')
        self.assertEqual(response.status_code, 404)


    def test_accessing_orders_with_invalid_or_expired_token(self):
        """ Tests accessing the orders endpoint with an invalid
        or expired token """
        response = self.client.get('/api/v2/orders/',
                                   headers={'Authorization':
                                            'XBA5567SJ2K119'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Token is invalid', str(response.data))

    def test_posting_an_order_with_invalid_or_expired_token(self):
        """ Tests accessing the orders endpoint with an invalid
        or expired token """
        response = self.client.post('/api/v2/users/orders',
                                   headers={'Authorization':
                                            'XBA5567SJ2K119'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Token is invalid',str(response.data))

    def test_create_an_order_for_non_menu_item(self):
        """ Tests placing an order with for non existant menu item """
        response = self.create_valid_order()
        self.assertEqual(response.status_code, 200)
        self.assertIn('"message": "Item Not Found"', str(response.data))


    def test_create_order_with_invalid_characters(self):
        """ Tests creating a menu with a invalid item_name or quantity """
        response = self.client.post('/api/v2/users/orders',
                                    data=json.dumps(self.invalid_order),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        self.assertEqual(response.status_code, 406)
 

    def test_create_order_with_invalid_quantiy(self):
        """ Tests creating a menu with a invalid item_name or quantity """
        response = self.client.post('/api/v2/users/orders',
                                    data=json.dumps(self.order_invalid_quantity),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        self.assertEqual(response.status_code, 406)
        self.assertIn('Quantity should be an integer', str(response.data))

    def test_get_all_orders(self):
        """ Tests a users getting all their orders """
        self.create_valid_order()
        response = self.client.get('/api/v2/users/orders',
                                   headers={'Authorization':
                                            self.get_token()})
        self.assertEqual(response.status_code, 200)

    def test_admin_get_all_orders(self):
        """ Tests admin getting all orders """
        self.create_valid_order()
        response = self.client.get('/api/v2/orders/',
                                   headers={'Authorization':
                                            self.get_token()})
        self.assertEqual(response.status_code, 200)

    def test_admin_get_specific_orders(self):
        """ Tests admin getting a specific order"""
        self.create_valid_menu()
        self.create_valid_order()
        response = self.client.get('/api/v2/orders/1',
                                   headers={'Authorization':
                                            self.get_token()})
        self.assertEqual(response.status_code, 200)

    def test_admin_updating_specific_orders(self):
        """ Tests admin updating a specific order"""
        self.create_valid_menu()
        self.create_valid_order()
        response = self.client.put('/api/v2/orders/1',
                                   data=json.dumps(self.valid_update),
                                   content_type='application/json',
                                   headers={'Authorization':
                                            self.get_token()})
        self.assertEqual(response.status_code, 200)