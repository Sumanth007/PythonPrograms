import sqlite3

conn = sqlite3.connect("D1.db")
print("Connection happended successfully")

conn.execute("DROP TABLE ST")
cursor = conn.execute("CREATE TABLE ST(ID INT PRIMARY KEY,NAME VARCHAR[50]);")
print("Table created successfully")

cursor.execute("INSERT INTO ST(ID,NAME) VALUES(1,'SUMANTH')")
cursor.execute("INSERT INTO ST(ID,NAME) VALUES(2,'SUMANTH')")

# s1 = cursor.execute("SELECT * FROM ST")
# for i in s1:
#     print(i[0]," -> ",i[1])
# s2 = cursor.execute("DELETE FROM ST WHERE id = 2")
# a = "-"
# print(a.center(100,"-"))
# s1 = cursor.execute("SELECT * FROM ST")
# for i in s1:
#     print(i[0]," -> ",i[1])
s2 = cursor.execute("SELECT ID FROM ST")

for i in s2:
    print(i)
conn.rollback()
cursor.close()
conn.close()

