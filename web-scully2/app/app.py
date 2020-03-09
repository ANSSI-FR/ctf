#!/usr/bin/python3
import sqlite3, os, hashlib
from flask import Flask, jsonify, render_template, request, g
from flag import flag

app = Flask(__name__)
app.database = "database.db"

@app.route('/')
def index():
    return render_template('index.html')

#API routes
@app.route('/api/v1/login/', methods=['POST'])
def login():
    if request.method == 'POST':
        username, password = (request.json['username'],request.json['password'])
        g.db = connect_db()
        try:
            cur = g.db.execute("SELECT * FROM players WHERE username = '{}' AND password = '{}'".format(username, hash_pass(password)))
            if cur.fetchone():
                result = {'status': 'success'}
            else:
                result = {'status': 'fail'}
        except sqlite3.OperationalError:
            result={'status': 'fail'}
        else:
            g.db.close()
        return jsonify(result)

@app.errorhandler(404)
def page_not_found_error(error):
    return render_template('error.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error=error)

def connect_db():
    return sqlite3.connect(app.database)

# Create password hashes
def hash_pass(password):
	return hashlib.sha256(password.encode('utf-8')).hexdigest()

if __name__ == "__main__":

    #create database if it doesn't exist yet
    if not os.path.exists(app.database):
        with sqlite3.connect(app.database) as connection:
            c = connection.cursor()
            c.execute("""CREATE TABLE players(id integer primary key autoincrement, username TEXT, password TEXT)""")
            c.execute('INSERT INTO players (username, password) VALUES("admin", "{}")'.format(hash_pass("ecsc1234$*")))
            c.execute('INSERT INTO players (username, password) VALUES("m.poole", "{}")'.format(hash_pass("badpassword")))
            c.execute('INSERT INTO players (username, password) VALUES("r.alexander", "{}")'.format(hash_pass("letmein")))
            c.execute('INSERT INTO players (username, password) VALUES("m.benson", "{}")'.format(hash_pass("P@$$w0rd")))
            c.execute("""CREATE TABLE flag(flag TEXT)""")
            c.execute('INSERT INTO flag (flag) VALUES("{}")'.format(flag))
            connection.commit()
            connection.close()

#    app.run(host='0.0.0.0') # runs on machine ip address to make it visible on netowrk
