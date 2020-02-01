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

def registerInDb(username,password,name,gender,email,hostel,room,institute):
	con = sql.connect("database.db")
	cur= con.cursor()
	cur.execute("INSERT INTO user (username,password,name,gender,email,hostel,room,institute) VALUES (?,?,?,?,?,?,?,?)",(username,password,name,gender,email,hostel,room,institute))

def reqInDB(username,recieptID,shirts,jeans,hoodies,sheets):
	con = sql.connect("database.db")
	cur= con.cursor()
	cur.execute("INSERT INTO reciept (username,recieptID,shirts,jeans,hoodies,sheets) VALUES (?,?,?,?,?,?)",(username,recieptID,shirts,jeans,hoodies,sheets))

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
		registerInDb(username,password,name,gender,email,hostel,room,institute)
		msg = 'registered successfully!!'
		return render_template('result.html',msg=msg)

@app.route('/req',methods = ['GET','POST'])
def req():
	if request.method == 'GET':
		return render_template('request.html')
	else:
		username = request.form['username']
		shirts = request.form['shirts-number']
		jeans = request.form['jeans-number']
		sheets = request.form['bedsheets-number']
		hoodies = request.form['hoodies-number']
		recieptID = request.form['recieptID']
		reqInDB(username,recieptID,shirts,jeans,hoodies,sheets)
		msg = f"order placed successfully!! and your reciept-ID is {recieptID}"
		return render_template('result.html',msg=msg)

@app.route('/reciept',methods=['GET'])
def reciept():
	return


@app.route('/fetchRec')
def fetchRec():
	con = sql.connect("database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from host")
	rows = cur.fetchall()
	cur.close()
	return (rows)

if __name__=='__main__':
	app.run(host='0.0.0.0', debug = True, port = 5000)
