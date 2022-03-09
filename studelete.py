import sqlite3

connection = sqlite3.connect("college.db")

getid = input("enter the student id: ")

connection.execute("delete from student where Id="+getid)
connection.commit()

print("Data deleted successfully")

result = connection.execute("select * from student")

print("data updated")

for i in result:
    print("Id =>",i[0])
    print("Name =>",i[1])
    print("Rollnumber =>",i[2])
    print("admino =>",i[3])
    print("College =>",i[4])
