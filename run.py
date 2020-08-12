import os
import psycopg2
from app import create_app
from app.database.database import *

app = create_app('DEFAULT')

"""Set your development database credentials"""
"""Example"""
"""db = Database('postgresql://YOUR_DATABASE_USERNAME:YOUR_DATABASE_PASSWORD@localhost:5432/YOUR_DATABASE_NAME')"""
db = Database('postgresql://admin:password@localhost:5432/order_db')

if __name__ == '__main__':

    db.create_tables()
    app.run(debug=True)
