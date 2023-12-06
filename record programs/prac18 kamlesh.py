import mysql.connector as mc
cn=mc.connect(host='localhost',password='kamlesh7madhu',username='root')
cr=cn.cursor()
cr.execute('Create database if not exists record')
cr.execute('Use record')
cr.execute('DROP table STUDENT')
cr.execute("Create table if not exists STUDENT(ROLL integer Primary Key,\
NAME varchar(30), TOTAL integer, COURSE varchar(20) CHECK(COURSE in\
('CS', 'BIOLOGY', 'COMMERCE', 'EG')), DOB DATE)")
cr.execute('Select * from student')
res=cr.fetchall()
if cr.rowcount==0:
    cr.execute("Insert into student values(1,'Rahul',460,'CS','2005-09-09')")
    cr.execute("Insert into student values(2,'Nikhil',380,'BIOLOGY','2005-06-29')")
    cr.execute("Insert into student values(3,'Arjun',477,'COMMERCE','2005-07-12')")
    cr.execute("Insert into student values(4,'Hari',443,'CS','2005-05-10')")
    cr.execute("Insert into student values(5,'Tharun',150,'EG','2003-05-20')")
    cn.commit()
cr.execute('Select * from student')
res=cr.fetchall()
no,marks={},[]
for i in range(len(res)):
    co=res[i][3]
    if co in no:
        no[co]=no[co]+1
    else:
        no[co]=1
    marks.append(res[i][2])
print('Maximum total marks',max(marks))
print('Minimum total marks',min(marks))
print('Number of students in courses with atleast 2 students')
for i in no:
    if no[i]>=2:
        print(i,':',no[i])
cr.execute("select * from student where total between 100 and 200 and dob like '2003-05-__'")
res1=cr.fetchall()
print("Details of students born in the month of may 2003 who have scored total between 100 to 200")
for i in res1:
    print(i[0],i[1],i[2],i[3],i[4])
print()
cr.execute("select * from student order by total desc")
res2=cr.fetchall()
print('Student list in the descending order of total')
for i in res2:
    print(i[0],i[1],i[2],i[3],i[4])
print()
print('Updating the table so that marks of CS students increased by 5% where marks less than 180')
cr.execute('Update student set total=1.05*total where total<180')
cn.commit()
cr.execute('Select * from student')
res=cr.fetchall()
print('Updated table')
for i in res:
    print(i[0],i[1],i[2],i[3],i[4])
print()
cn.close()
