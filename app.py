import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from --your name-- in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://hello_flask_database_user:74vGGSDNl3DGhVRLs0hn26KgxfRsXsQ2@dpg-cqlbg4d6l47c73ao847g-a/hello_flask_database")
    conn.close()
    return "Database Connection Successfull"
