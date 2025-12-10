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
# 메인페이지
@app.route('/')
def index():
    keyword = request.args.get('keyword', '')
    conn = get_db()
    if keyword:
        shoes = conn.execute(
            'SELECT * FROM shoes WHERE name LIKE ? OR experience LIKE ? ORDER BY name',
            ('%'+keyword+'%', '%'+keyword+'%')
        ).fetchall()
    else:
        shoes = conn.execute('SELECT * FROM shoes ORDER BY name').fetchall()
    
    conn.close()
    return render_template('base.html', shoes=shoes, keyword=keyword)