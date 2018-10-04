from flask import json
from test_base import TestBase


class TestMenu(TestBase):
    """ Defines tests for the view methods of menu """

    def setUp(self):
        self.create_valid_user()

    def test_accessing_menu_view_without_token(self):
        """ Tests accessing the menu endpoint without a token """
        response = self.client.get('/api/v2/menu')
        self.assertEqual(response.status_code, 401)

    def test_accessing_menu_view_with_invalid_or_expired_token(self):
        """ Tests accessing the menu endpoint with an invalid
        or expired token """
        response = self.client.get('/api/v2/menu',
                                   headers={'Authorization':
                                            'XBA5567SJ2K119'})
        self.assertEqual(response.status_code, 401)



    def test_create_menu_with_valid_details(self):
        """ Tests adding a menu with valid details """
        response = self.create_post_menu()
        self.assertEqual(response.status_code, 201)
        self.assertIn('You added a food item successfully.',str(response.data))

    def test_create_menu_with_blank_attributes(self):
        """ Tests creating a menu with a blank item name or price """
        menu = {
            'item_name': '',
            'price': '',
        }
        response = self.client.post('/api/v2/menu',
                                    data=json.dumps(menu),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        self.assertEqual(response.status_code, 406)

    def test_create_menu_with_invalid_characters(self):
        """ Tests creating a menu with a blank item name or price """
        menu = {
            'item_name': '@#$%',
            'price': '@#$%',
        }
        response = self.client.post('/api/v2/menu',
                                    data=json.dumps(menu),
                                    content_type='application/json',
                                    headers={'Authorization':
                                             self.get_token()})
        self.assertEqual(response.status_code, 406)

    def test_create_duplicate_menu(self):
        """ Tests creating a duplicate menu(same attributes) """
        self.create_valid_menu()
        response = self.create_valid_menu()
        self.assertEqual(response.status_code, 409)

    def test_get_menu(self):
        """ Tests fetching all menu """
        self.create_valid_menu()
        response = self.client.get('/api/v2/menu',
                                   headers={'Authorization':
                                            self.get_token()})
        self.assertEqual(response.status_code, 200)