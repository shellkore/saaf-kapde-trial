from flask import Flask, render_template, request, redirect,url_for,jsonify
import sqlite3 as sql
import time
import os

app = Flask(__name__)

def registerInDb(username,password,name,gender,email,hostel,room,institute):
	con = sql.connect("database.db")
	cur= con.cursor()
	cur.execute("INSERT INTO user (username,password,name,gender,email,hostel,room,institute) VALUES (?,?,?,?,?,?,?,?)",(username,password,name,gender,email,hostel,room,institute))
	con.commit()
	cur.close()
	return("registered in Database")

def reqInDB(username,recieptID,shirts,jeans,hoodies,sheets):
	con = sql.connect("database.db")
	cur= con.cursor()
	cur.execute("INSERT INTO reciept (username,recieptID,shirts,jeans,hoodies,sheets) VALUES (?,?,?,?,?,?)",(username,recieptID,shirts,jeans,hoodies,sheets))
	con.commit()
	cur.close()
	return("request saved in Database")

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
		print(reqInDB(username,recieptID,shirts,jeans,hoodies,sheets))
		msg = f"order placed successfully!! and your reciept-ID is {recieptID}"
		return render_template('result.html',msg=msg)

@app.route('/reciept',methods=['GET'])
def reciept():
	return render_template('reciept.html')


@app.route('/fetchRec',methods=['POST'])
def fetchRec():
	#8f3xgv
	rID = request.form.get('rId')
	print(rID)
	con = sql.connect("database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute(f"select * from reciept where recieptID='{rID}'")
	rows = cur.fetchall()
	print(len(rows[0]))
	cur.close()

	shirts = rows[0][2]
	jeans = rows[0][3]
	hoodies = rows[0][4]
	sheets = rows[0][5]
	return (jsonify([shirts,jeans,hoodies,sheets]))
	# return ('sending...')

@app.route('/pricing',methods=['GET'])
def pricing():
	return render_template('pricing.html')

@app.route('/contact',methods=['GET'])
def contact():
	return render_template('contact_us.html')

if __name__=='__main__':
	app.run(host='0.0.0.0', debug = True, port = 5000)
