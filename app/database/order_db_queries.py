"""This module handles order queries"""
from urllib.parse import urlparse
import psycopg2
from werkzeug.security import generate_password_hash
from flask import current_app as app
from .database import Database


class OrderDbQueries(Database):
    """This class handles database transactions for the order"""

    def __init__(self):
        Database.__init__(self, app.config['DATABASE_URL'])

    def insert_order_data(self, data, username):
        """Insert a new order record to the database"""
        query = "INSERT INTO orders (item_name, quantity, username, status)\
        VALUES('{}', '{}', '{}', '{}');".format(data['item_name'], data['quantity'], username, 'New')
        self.cur.execute(query)
        self.conn.commit()

    def fetch_all_orders(self):
        """ Fetches all order recods from the database"""
        self.cur.execute("SELECT * FROM orders ")
        rows = self.cur.fetchall()
        orders = []
        for row in rows:
            row = {'orderId': row[0], 'item_name': row[1],
                   'quantity': row[2],
                    "username": row[3], 'status': row[4],
                   }
            orders.append(row)
        return orders

    def fetch_all_orders_by_parameter(self, table_name, column, param):
        """Fetches a single a parameter from a specific table and column"""
        query = "SELECT * FROM {} WHERE {} = '{}'".format(table_name, column, param)
        self.cur.execute(query)
        rows = self.cur.fetchall()
        orders = []
        for row in rows:
            row = {'orderId': row[0], 'item_name': row[1], 'quantity': row[2], 'username' : row[3], 'status' : row[4]}
            orders.append(row)
        return orders

    def get_by_argument(self, table, column_name,argument):
        query = "SELECT * FROM {} WHERE {} = '{}';".format(table, column_name, argument)
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result

    def update_order_status(self, orderId):
        orders = OrderDbQueries().fetch_all_orders_by_parameter('orders', 'orderId', orderId)
        for order in orders:
            if orderId:
                if order['status'] == 'New':
                    query = "UPDATE orders SET status = 'Processing' WHERE orderId = orderId"
                    self.cur.execute(query)
                elif order['status'] == 'Processing':
                    query = "UPDATE orders SET status = 'Completed' WHERE orderId = orderId"
                    self.cur.execute(query)
