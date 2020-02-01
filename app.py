from flask import Flask, render_template, request, redirect,url_for
import sqlite3 as sql
import time
import os

app = Flask(__name__)

def dbHandler():
	con = sql.connect("database.db")
	cur=con.cursor()
	cur.execute("select name from host")
	return

def registerInDb(name,gender,email,hostel,room,institute):


@app.route('/',methods = ['GET'])
def home():
	return render_template('index.html')

@app.route('/register',methods = ['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	else:
		username = request.form['username']
		password = request.form['password']
		name = request.form['firstname']
		gender = request.form['gender']
		email = request.form['email']
		hostel = request.form['hostel-name']
		room = request.form['room-no']
		institute = request.form['institute-name']	

		msg = 'registered successfully'
		return render_template('result.html',msg=msg)

if __name__=='__main__':
	app.run(host='0.0.0.0', debug = True, port = 5000)
