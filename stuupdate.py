import sqlite3

connection = sqlite3.connect("college.db")

getid = input("enter the id")
getname = input("enter the name")
getrollnumber = input("enter the rollnumber")
getadmino = input("enter the admino")
getcollege = input("enter the college")

result = connection.execute("update student set Name='"+getname+"',Rollnumber="+getrollnumber+",admino="+getadmino+",College='"+getcollege+"' where Id="+getid+"")
connection.commit()

print("data updated successfully")
result = connection.execute("select * from student where Id="+getid+"")

print("data updated")

for i in result:
    print("id =>", i[0])
    print("Name =>", i[1])
    print("Rollnumber =>", i[2])
    print("admino =>", i[3])
    print("College =>", i[4])
