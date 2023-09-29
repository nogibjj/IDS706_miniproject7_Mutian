"""
ETL-Query script
"""

import sqlite3

def connectDB(name):
    # connect to a SQLite data base
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    return conn,cursor
def createDB(cursor):
    # create a table
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS students(
                    id INTEGER PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    age INTEGER,
                    classno INTEGER
                ) 
                   ''')
def readDB(cursor):
    # read all data from table
    
    cursor.execute('SELECT * FROM students')
    return cursor.fetchall()

def updateDB(cursor,id,first_name,last_name,age,classno):
    # update student info
    updatequery = '''
    UPDATE students 
    SET first_name= '{}',
    last_name = '{}',
    age = '{}' ,
    classno = '{}' 
    WHERE id = '{}'
    '''.format(first_name,last_name,age,classno,id)
    cursor.execute(updatequery)
    # cursor.execute('''UPDATE students 
    #                SET first_name= ?,
    #                last_name = ?,
    #                age = ? ,
    #                classno = ? 
    #                WHERE id = ? ''',(first_name,last_name,age,classno,id,))
def deleteDB(cursor,id):
    # delete a data from table
    cursor.execute('DELETE FROM students WHERE id = ?',(id,))
    
def insertDB(cursor,id,first_name,last_name,age,classno):
     cursor.execute('''INSERT INTO students VALUES (?,?,?,?,?)''',(id,first_name,last_name,age,classno))
    
    