"""
Test goes here

"""

from mylib.dbfunc import connectDB, createDB, insertDB, readDB, updateDB, deleteDB

import os


def test_create():
    if os.path.exists("mydb.db"):
        os.remove("mydb.db")
    conn, cursor = connectDB("mydb.db")
    assert os.path.exists("mydb.db")
    createDB(cursor)

    table_name = "students"
    cursor.execute(f"PRAGMA table_info({table_name})")
    result = cursor.fetchall()
    assert result is not None


def test_insert():
    if os.path.exists("mydb.db"):
        os.remove("mydb.db")
    conn, cursor = connectDB("mydb.db")
    createDB(cursor)
    insertDB(cursor, 1, "Ethan", "Smith", 20, 1)
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchone()
    assert result is not None


def test_read():
    if os.path.exists("mydb.db"):
        os.remove("mydb.db")
    conn, cursor = connectDB("mydb.db")
    createDB(cursor)
    insertDB(cursor, 1, "Ethan", "Smith", 20, 1)
    insertDB(cursor, 2, "Emma", "Brown", 21, 2)
    insertDB(cursor, 3, "Lucas", "Davis", 18, 3)

    info = readDB(cursor)
    assert len(info) == 3


def test_update():
    if os.path.exists("mydb.db"):
        os.remove("mydb.db")
    conn, cursor = connectDB("mydb.db")
    createDB(cursor)
    insertDB(cursor, 1, "Ethan", "Smith", 20, 1)
    insertDB(cursor, 2, "Emma", "Brown", 21, 2)
    insertDB(cursor, 3, "Lucas", "Davis", 18, 3)

    updateDB(cursor, 1, "Ethan", "James", 23, 5)
    info = readDB(cursor)
    assert info[0] == (1, "Ethan", "James", 23, 5)


def test_delete():
    if os.path.exists("mydb.db"):
        os.remove("mydb.db")
    conn, cursor = connectDB("mydb.db")
    createDB(cursor)
    insertDB(cursor, 1, "Ethan", "Smith", 20, 1)
    insertDB(cursor, 2, "Emma", "Brown", 21, 2)
    insertDB(cursor, 3, "Lucas", "Davis", 18, 3)

    deleteDB(cursor, 1)
    deleteDB(cursor, 2)
    deleteDB(cursor, 3)
    info = readDB(cursor)
    assert len(info) == 0
