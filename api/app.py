import sqlite3
from flask import Flask, g, jsonify, request
from pathlib import Path
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
DATABASE = str(Path('../storage/db.sqlite3'))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def hello_world():
    cur = get_db().cursor()
    cur.execute('select * from bans ORDER BY(ban_date) desc limit 5 ')
    return jsonify(cur.fetchall())

@app.route('/search')
def searchBans():
    reason = request.args.get('reason')
    cur = get_db().cursor()
    cur.execute('select * from bans limit 5 where reason l ')
    cur = get_db().cursor()
    return ''

@app.route('/messages')
def messages():
    cur = get_db().cursor()
    cur.execute('select * from ic_events limit 5')
    return jsonify(cur.fetchall())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)