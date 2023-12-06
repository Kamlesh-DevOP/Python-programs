import mysql.connector as mc
cn=mc.connect(host='localhost',password='kamlesh7madhu',username='root')
cr=cn.cursor()
cr.execute('Create database if not exists record')
cr.execute('Use record')
cr.execute('drop table employee')
cr.execute("Create table if not exists Employee(Empno integer Primary Key,\
Name varchar(30), Desig varchar(30), Deptno integer, Salary integer)")
cr.execute("Create table if not exists Department(Deptno integer, Dname varchar(30), Location varchar(60))")
cr.execute('Select * from Employee')
res=cr.fetchall()
if cr.rowcount==0:
    cr.execute("Insert into Employee values(1,'Rohan','Admin',100,70000)")
    cr.execute("Insert into Employee values(2,'Sundar','Manager',101,69000)")
    cr.execute("Insert into Employee values(3,'Arjun','Manager',102,42000)")
    cr.execute("Insert into Employee values(4,'Shankar','Financier',101,57000)")
    cr.execute("Insert into Employee values(5,'Madhu','Admin',100,77000)")
    cn.commit()
cr.execute('Select * from Department')
res=cr.fetchall()
if cr.rowcount==0:
    cr.execute("Insert into Department values(100,'IT','Block A')")
    cr.execute("Insert into Department values(101,'Advisor','Block A')")
    cr.execute("Insert into Department values(102,'Sales','Block C')")
    cr.execute("Insert into Department values(103,'HR','Block B')")
    cn.commit()
cr.execute('Select * from Employee e,Department t where e.deptno=t.deptno')
res=cr.fetchall()
print('Joined tables')
for i in res:
    for j in i:
        print(j,end=' ')
    print()
cr.execute("Select Empno,Name, Salary, Dname, Location from Employee e,Department t where e.deptno=t.deptno and desig='Manager'")
res=cr.fetchall()
print('Details of all managers')
for i in res:
    for j in i:
        print(j,end=' ')
    print()
cn.close()