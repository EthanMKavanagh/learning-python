from flask import Flask
import psycopg2
app = Flask(__name__)

# use our connection values to establish a connection
con = psycopg2.connect(
    user = 'ethankavanagh',
    host = 'localhost',
    port = 5432,
    database = 'python3_db'
)
# create a psycopg2 cursor that can execute queries
cur = con.cursor()

@app.route('/')
def helloWorld():
    return "Hello World!"

@app.route('/messages')
def message():
    cur.execute("SELECT * FROM python")
    rows = cur.fetchall()
    print ('These are the rows:', rows)
    for r in rows:
        return (f"{r[1]} - {r[2]}")
        # return (r[1] + ' - ' + r[2])
    cur.close()
    con.close()