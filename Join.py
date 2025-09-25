import sqlite3
con=sqlite3.connect("sqlite.db")
print("STUDENT_ID", "STUDENT_Name", "STUDENT_Fees")
db=con.execute("SELECT f.st_id, FROM fees as f in inner join student as s on f.st_id=s.st_id")

for a in db:
    print(a)
con.close()