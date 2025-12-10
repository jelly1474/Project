from flask import Flask, render_template, request, redirect
import sqlite3
import csv

app = Flask(__name__)
DATABASE = 'shoes.db'


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS shoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            price REAL,
            experience TEXT,
            weight REAL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    keyword = request.args.get('keyword', '').strip()
    conn = get_db()
    
    base_sql = "SELECT * FROM shoes"
    params = []

    if keyword:
        base_sql += " WHERE name LIKE ? OR experience LIKE ?"
        like_kw = f"%{keyword}%"
        params.extend([like_kw, like_kw])

    base_sql += " ORDER BY name"

    shoes = conn.execute(base_sql, params).fetchall()
    
    conn.close()
    return render_template('base.html', shoes=shoes, keyword=keyword)