import csv
with open('csvfile.csv','w+') as f:
    writer=csv.writer(f)
    writer.writerow(['sno','name','salary'])
    L=[]
    for i in range(3):
        sno=int(input('enter sno: '))
        name=input('Enter name: ')
        sal=int(input('enter salary: '))
        L+=[[sno,name,sal]]
    writer.writerows(L)
    content=csv.reader(f)
    f.tell()
    for i in content:
        print(i)

