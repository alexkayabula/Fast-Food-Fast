import os
import psycopg2
from app import create_app
from app.database.database import Database

app = create_app('PRODUCTION')
db = Database('postgres://eyzxekqeckzgjc:78e620ab085ae62514bd49db48ce33ec3c50df764c5822e6d8ec9d7607527534@ec2-23-23-80-20.compute-1.amazonaws.com:5432/dac1le4vb3d4of')

if __name__ == '__main__':
    db.create_database('order_db')
    db.create_tables()
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port)
