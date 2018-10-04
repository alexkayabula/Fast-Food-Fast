"""This module handles menu queries"""
from urllib.parse import urlparse
import psycopg2
from werkzeug.security import generate_password_hash
from flask import current_app as app
from database import Database


class MenuDbQueries(Database):
    """This class handles database transactions for the menu"""

    def __init__(self):
        Database.__init__(self, app.config['DATABASE_URL'])

    def insert_menu_data(self, data):
        """Insert a new menu item to the database"""
        query = "INSERT INTO menu (item_name, price)\
        VALUES('{}', '{}');".format(data['item_name'], data['price'])
        self.cur.execute(query)
        self.conn.commit()

    def fetch_all_menu(self):
        """ Fetches all order recods from the database"""
        self.cur.execute("SELECT * FROM menu ")
        rows = self.cur.fetchall()
        orders = []
        for row in rows:
            row = {'menu_id': row[0], 'item_name': row[1], 'price': row[2]}
            orders.append(row)
        return orders