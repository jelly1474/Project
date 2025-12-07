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
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()
