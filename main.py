from flask import Flask, render_template
import os
import sqlite3

app = Flask(__name__)

app.config.update(dict(
   SECRET_KEY='sosecret',
   DATABASE=os.path.join(app.root_path, 'flask_dojo.db'),
   SITE_NAME='TO-DO App'
))


def create_database(database_path):
   """Creates database, drops one if exists."""
   conn = sqlite3.connect(database_path)
   c = conn.cursor()
   c.execute('''DROP TABLE IF EXISTS dojo;''')
   c.execute('''CREATE TABLE dojo(count INT );''')
   c.execute('''INSERT INTO dojo(count) VALUES (0);''')
   conn.commit()
   conn.close()


create_database(os.path.join(app.root_path, 'flask_dojo.db'))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/request-counter", methods=['GET', 'POST'])
def counting():
    conn = sqlite3.connect(os.path.join(app.root_path, 'flask_dojo.db'))
    c = conn.cursor()
    n = 1
    while True:

        c.execute('''Update dojo SET count = {}'''.format(n))
        n += 1
        break
    conn.commit()
    conn.close()
    return render_template("counter.html")

app.run(debug=True)