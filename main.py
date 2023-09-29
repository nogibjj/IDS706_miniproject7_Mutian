from mylib.dbfunc import connectDB, createDB, insertDB, readDB, updateDB, deleteDB
import os


if os.path.exists("mydb.db"):
    os.remove("mydb.db")
conn, cursor = connectDB("mydb.db")

# C
createDB(cursor)
insertDB(cursor, 1, "Ethan", "Smith", 20, 1)
insertDB(cursor, 2, "Emma", "Brown", 21, 2)
insertDB(cursor, 3, "Lucas", "Davis", 18, 3)
# R
info = readDB(cursor)

print(info)

# U
updateDB(cursor, 1, "Ethan", "James", 23, 5)
info = readDB(cursor)
print(info)


# D
deleteDB(cursor, 2)
info = readDB(cursor)
print(info)


conn.commit()
conn.close()
