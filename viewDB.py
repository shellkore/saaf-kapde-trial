import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

print("reciept DB.....")
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("select * from reciept")
rows= cur.fetchall()
print(rows)
for row in rows:
	for col in row:
		print(col)
cur.close()
