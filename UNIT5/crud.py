import sqlite3

connection = sqlite3.connect("books.db")
print("Connection completed successfully")

connection.execute("DROP TABLE BOOKS")
cursor = connection.execute("CREATE TABLE BOOKS(ID INT PRIMARY KEY,NAME VARCHAR[50],AUTHOR VARCHAR[50],COPIES [100]);")

cursor.execute("INSERT INTO BOOKS VALUES(1,'FISH EYE','ROXOR',108)")
cursor.execute("INSERT INTO BOOKS VALUES(2,'FISH EYE','ROXOR',108)")
cursor.execute("INSERT INTO BOOKS VALUES(3,'FISH EYE','ROXOR',108)")
cursor.execute("INSERT INTO BOOKS VALUES(4,'FISH EYE','ROXOR',108)")

display = cursor.execute("SELECT NAME FROM BOOKS WHERE ID = 3")
for row in display:
    print(row[0])


print(type(connection))
connection.commit()
connection.close()