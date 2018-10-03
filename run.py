import os
import psycopg2
from app import create_app
from app.database import Database

app = create_app('DEFAULT')
db = Database('postgresql://postgres:k0779211758aj@localhost:5432/order_db')

if __name__ == '__main__':
    
    db.create_tables()
    app.run(debug=True)