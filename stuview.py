import sqlite3

connection = sqlite3.connect("college.db")

result = connection.execute("select * from student")

for i in result:
    print("id =>", i[0])
    print("Name =>", i[1])
    print("Rollnumber =>", i[2])
    print("admino =>", i[3])
    print("College =>", i[4])
