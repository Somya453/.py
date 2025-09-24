import sqlite3
con=sqlite3.connect("sqlite.db")

# con.execute('''
#     Create table student(
#     st_id INT AUTO_INCREMENT PRIMARY KEY,
#     st_name VARCHAR(50),
#     st_email VARCHAR(20),
#     st_class VARCHAR(10))
# ''')


#insert query
insert='''
    insert into student(st_name, st_class, st_email) VALUES ('MANAN', '11th', "manan@123gmail.com")
'''

con.execute(insert)
con.commit()
# con.close()


# select query
data=con.execute("SELECT * FROM student")

for n in data:  #get data
    print(n)


print("Student_id", "student_email")
print(n[0], "   ", n[1], "   ", n[2],n[3])


# limit data
dat=con.execute("SELECT * FROM student limit 0,2")
print(dat)

# delete 
# st_id=input("Enter Student id:")
# con.execute("DELETE FROM student where st_id="+st_id)
# con.commit()
# con.close()


#update
con.execute('''
    update student set st_name='mayank' st_id=2
''')
con.commit()
con.close()