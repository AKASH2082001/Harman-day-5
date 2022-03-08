import sqlite3

connection = sqlite3.connect("college.db")

# connection.execute('''  Create Table Student(
#                   Id integer primary key autoincrement,
#                   Name text,
#                   Rollnumber integer,
#                   admino integer,
#                   College text
#
# )''')
#
# print("Table Created Sucessfully")

getname = input("enter the name")
getrollnumber = input("enter the rollnumber")
getadmino = input("enter the admino")
getcollege = input("enter the college")
connection.execute("Insert into student(Name,Rollnumber,Admino,College) values('"+getname+"',"+getrollnumber+","+getadmino+",'"+getcollege+"')")

connection.commit()
connection.close()

print("Inserted Sucessfully")