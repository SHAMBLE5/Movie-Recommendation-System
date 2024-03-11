import sqlite3

conn = sqlite3.connect('feed.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE students(name TEXT, model TEXT, km TEXT, feedback TEXT)')
print ("Table created successfully");
