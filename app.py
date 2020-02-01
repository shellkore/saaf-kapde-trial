from flask import Flask, render_template, request, redirect,url_for
import sqlite3 as sql
import time
import os

app = Flask(__name__)

def dbHandler():
	con = sql.connect("database.db")
	cur=con.cursor()
	cur.execute("select name from host")

@app.route('/',methods = ['GET'])
def home():
	return render_template('index.html')

@app.route('/',methods = ['GET,POST'])
def register():
	if method == 'GET':
		return render_template(register.html)

if __name__=='__main__':
	app.run(host='0.0.0.0', debug = True, port = 5000)
