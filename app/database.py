"""This module handles database queries"""
from urllib.parse import urlparse
import psycopg2
from werkzeug.security import generate_password_hash
from flask import current_app as app


class Database:
    """This class does all database related stuff"""

    def __init__(self, database_url):
        """Initializes the connection url"""
        parsed_url = urlparse(database_url)
        d_b = parsed_url.path[1:]
        username = parsed_url.username
        hostname = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port

        self.conn = psycopg2.connect(
            database=d_b, user=username, password=password,
            host=hostname, port=port)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def create_database(self, db_name):
        """Creates a database to be used in production"""
        self.cur.execute('CREATE DATABASE {};'.format(db_name))

    def trancate_table(self, table):
        """Trancates the table"""
        self.cur.execute("TRUNCATE TABLE {} RESTART IDENTITY".format(table))

    def create_tables(self):
        """Creates database tables """
        create_table = "CREATE TABLE IF NOT EXISTS users\
        (user_id SERIAL PRIMARY KEY, name text , username text UNIQUE, password text , admin_status boolean)"
        self.cur.execute(create_table)
        try:
           query = "INSERT INTO users (name, username, password, admin_status)\
           VALUES('{}','{}', '{}', '{}');".format('admin', 'admin', generate_password_hash('admin'), True)
           self.cur.execute(query)                      
        except ( Exception, psycopg2.DatabaseError):
            pass
        
        create_table = "CREATE TABLE IF NOT EXISTS orders\
        (orderId SERIAL PRIMARY KEY, item_name text,\
        quantity text, username text, status text)"
        self.cur.execute(create_table)


        create_table = "CREATE TABLE IF NOT EXISTS menu\
        (menu_id SERIAL PRIMARY KEY, item_name text, price\
        text)"
        self.cur.execute(create_table)


    def fetch_by_parameter(self, table_name, column, param):
        """Fetches a single a parameter from a specific table and column"""
        query = "SELECT * FROM {} WHERE {} = '{}'".format(table_name, column, param)
        self.cur.execute(query)
        row = self.cur.fetchone()
        return row


class UserDbQueries(Database):
    """This class handles database transactions for the user"""

    def __init__(self):
        Database.__init__(self, app.config['DATABASE_URL'])

    def insert_user_data(self, data):
        query = "INSERT INTO users (name, username, password, admin_status)\
            VALUES('{}','{}', '{}', '{}');".format(data['name'],
                                             data['username'],
                                             generate_password_hash
                                             (data['password']), False)
        self.cur.execute(query)
        self.conn.commit()
        
    def fetch_all_users(self):
        """ Fetches all order recods from the database"""
        self.cur.execute("SELECT * FROM users ")
        rows = self.cur.fetchall()
        users = []
        for row in rows:
            row = {'user_id': row[0], 'name': row[1], 'username': row[2], 'admin_status': row[3]}
            users.append(row)
        return users


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