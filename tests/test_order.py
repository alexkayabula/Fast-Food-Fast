from flask import json, jsonify
import uuid
from test_data import*
from test_base import TestBase


class TestOrder(TestBase):

    def test_order_creation(self):
        """Test API can create a order (POST request)"""
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(test_order1))
        self.assertEqual(response.status_code, 201)
        self.assertIn('Order Made Successfully', str(response.data))

    def test_order_creation_given_past_order(self):
        """Test if a order can be created with a past order"""
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(past_order_date))
        self.assertIn("Order cannot have a past date", str(response.data))

    def test_duplicate_order_creation(self):
        """Test if a duplicate order can be created"""
        self.client.post('api/v1/orders/',
                         content_type='application/json',
                         data=json.dumps(duplicate_order))
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(duplicate_order))
        self.assertIn("Order Already Exists", str(response.data))

    def test_get_all_orders(self):
        """Test to get all orderss"""
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(test_order2))
        self.assertEqual(response.status_code, 201)
        response = self.client.get('api/v1/orders/')
        self.assertEqual(response.status_code, 200)

    def test_for_empty_input_fields(self):
        """Test for empty fields"""
        self.client.post('api/v1/orders/',
                         content_type='application/json',
                         data=json.dumps(test_empty_order))
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(test_empty_order))
        self.assertIn("All fields are required", str(response.data))
        self.assertEqual(response.status_code, 406)

    def test_for_invalid_item_name(self):
        """Test for invalid item_name"""
        self.client.post('api/v1/orders/',
                         content_type='application/json',
                         data=json.dumps(test_invalid_order1))
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(test_invalid_order1))
        self.assertIn("Item name should only contain alphabetic characters",
                      str(response.data))
        self.assertEqual(response.status_code, 406)

    def test_for_invalid_user_name(self):
        """Test for invalid user_name"""
        self.client.post('api/v1/orders/',
                         content_type='application/json',
                         data=json.dumps(test_invalid_order2))
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(test_invalid_order2))
        self.assertIn("Username should only contain alphabetic characters",
                      str(response.data))
        self.assertEqual(response.status_code, 406)

    def test_for_invalid_price(self):
        """Test for invalid price type"""
        self.client.post('api/v1/orders/',
                         content_type='application/json',
                         data=json.dumps(test_invalid_order3))
        response = self.client.post('api/v1/orders/',
                                    content_type='application/json',
                                    data=json.dumps(test_invalid_order3))
        self.assertIn("Price should only contain Numeric characters",
                      str(response.data))
        self.assertEqual(response.status_code, 406)

    def test_get_order_by_id(self):
        """Test to get order by id"""
        self.client.post('api/v1/orders/',
                         content_type='application/json',
                         data=json.dumps(test_order_id))
        response = self.client.get('api/v1/orders/')
        self.assertEqual(response.status_code, 200)
        order_id = test_order_id['order_id']
        response = self.client.get('api/v1/orders/{}'.format(order_id))
        self.assertEqual(response.status_code, 404)
