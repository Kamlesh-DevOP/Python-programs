import csv
with open('csvfile.csv','r+',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['sno','name','salary'])
    L=[]
    for i in range(2):
        sno=int(input('enter sno: '))
        name=input('Enter name: ')
        sal=int(input('enter salary: '))
        L+=[[sno,name,sal]]
    writer.writerows(L)
    content=csv.reader(f)
    print(f.tell())
    f.seek(0)
    for i in content:
        print(i)

