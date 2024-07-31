import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from --your name-- in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("your_db_url_here")
    conn.close()
    return "Database Connection Successfull"
