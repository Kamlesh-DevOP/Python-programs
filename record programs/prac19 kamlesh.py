import mysql.connector as mc
import csv
f=open('Student.csv','w',newline='')
wr=csv.writer(f)
cn=mc.connect(host='localhost',password='kamlesh7madhu',username='root', database='record')
cr=cn.cursor()
cr.execute('Select * from student')
res=cr.fetchall()
for i in res:
    wr.writerow(i)
f.close()
print('Details of all students')
f=open('Student.csv','r')
rr=csv.reader(f)
for i in rr:
    print(i[0],i[1],i[2],i[3],i[4],sep=',')
f.close()
marks=[]
f=open('Student.csv','r')
rr=csv.reader(f)
print('Top scorer name: ', end=' ')
for i in range(len(res)):
    marks.append(int(res[i][2]))
maxm=max(marks)
for i in rr:
    if int(i[2])==maxm:
        print(i[1])
