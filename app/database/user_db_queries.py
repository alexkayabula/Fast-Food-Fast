"""This module handles user queries"""
from urllib.parse import urlparse
import psycopg2
from werkzeug.security import generate_password_hash
from flask import current_app as app
from database import Database

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
