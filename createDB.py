import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

# conn.execute('CREATE TABLE host (name TEXT, email TEXT, phone INTEGER NOT NULL PRIMARY KEY,address TEXT)')
# print ("Table host created successfully")

# conn.execute('CREATE TABLE visitor (name TEXT, email TEXT, phone INTEGER NOT NULL PRIMARY KEY, host TEXT, checkin TEXT, checkout TEXT)')
# print("table visitor created successfully")
# conn.close()

conn.execute('CREATE TABLE user (username TEXT,password TEXT, name TEXT, gender TEXT,email TEXT, hostel TEXT, room TEXT, institute TEXT)')
print("user table created successfully!")

conn.execute('CREATE TABLE reciept(username TEXT,recieptID TEXT,shirts INTEGER,jeans INTEGER,hoodies INTEGER,sheets INTEGER)')
print("reciept table  created succefully!")
conn.close()
#firstname
#gender
#email
#hostel
#room
#institute