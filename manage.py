import os
import psycopg2
from app import create_app
from app.database.database import Database

app = create_app('PRODUCTION')
db = Database('postgres://xarplzfllomlvr:b52cdb7c12c1d0175f7569876e8ceaae7d36a3387b93b876f58c67839c95b9a2@ec2-107-22-175-33.compute-1.amazonaws.com:5432/d498qmhc8lmfvk')

if __name__ == '__main__':
    db.create_tables()
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port)
