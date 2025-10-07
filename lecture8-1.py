
'''Database programming means writing Python code to store, retrieve, update, and delete data from a database — 
usually using SQL (Structured Query Language).

Connect --	Establish connection to DB
Cursor --	Execute SQL commands
Execute --	Run INSERT, SELECT, UPDATE, DELETE
Commit --	Save changes to disk
Close --	Free resources

'''

#we can work on our own offline database as well as online present databases.

import sqlite3
try: 
    connection = sqlite3.connect('mydata.db') #parameter passed is database name
    cursor = connection.cursor() #cursor is used to execute the sql commands

    #create a new table in database

    query1 = """CREATE TABLE IF NOT EXISTS
    Persons (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name VARCHAR(32), last_name VARCHAR(32), age INTEGER, location TEXT)"""

    query2 = """INSERT INTO Persons
    (first_name, last_name, age, location)
    VALUES
    ('Hassan', 'Shahzad', 21, 'Lahore'),
    ('Ibad', 'Adrees', 20, 'Lahore'),
    ('Ali', 'Adrees', 18, 'Lahore'),
    ('Ahmed', 'Khan', 25, 'Karachi'),
    ('Sara', 'Malik', 23, 'Islamabad'),
    ('Usman', 'Tariq', 27, 'Faisalabad'),
    ('Mariam', 'Saleem', 22, 'Rawalpindi'),
    ('Bilal', 'Qureshi', 30, 'Multan'),
    ('Ayesha', 'Zafar', 19, 'Hyderabad'),
    ('Omar', 'Rashid', 24, 'Quetta'),
    ('Fatima', 'Saeed', 26, 'Sialkot'),
    ('Zain', 'Butt', 29, 'Gujranwala'),
    ('Hiba', 'Ali', 28, 'Peshawar')"""

    query3 = """SELECT * FROM Persons"""

    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    rows = cursor.fetchall() #fetchall() only works after a query that returns data (like SELECT). If you use it after an INSERT, UPDATE, or DELETE, it will cause error
    print(rows)
    connection.commit()

except Exception as e:
    print(e)

finally:
    connection.close()
