'''
C)Write a menu based program to do the following
a. Create_Bin() - To create a binary file of (EmpId, EmpName, Designation )
b. Insert() : To insert before a particular record. (when name is given)
c. Del_Record() : To Delete a record when the name is given
'''
import pickle,os
def Create_Bin(n):
    with open('employee details.dat','wb') as f:
        for i in range(n):
                empid=int(input('Enter employee id: '))
                empname=input('Enter employee name: ').capitalize()
                desig=input('Enter designation: ').capitalize()
                l=[empid,empname,desig]
                pickle.dump(l,f)
    print('File contents: ')
    with open('employee details.dat','rb') as f:
        try:
            while True:
                l=pickle.load(f)
                print(l)
        except: pass


def Insert():
    posname=input('Before which record do you want to insert the new record: ' ).capitalize()
    newempid=int(input('Enter new employee id: '))
    newempname=input('Enter new employee name: ').capitalize()
    newdesig=input('Enter new designation: ').capitalize()
    newrec=[newempid,newempname,newdesig]
    with open('employee details.dat','rb') as f, open('Temp.dat','wb') as f1:
        try:
            while True:
                l=pickle.load(f)
                if l[1]!=posname:
                    pickle.dump(l,f1)
                else:
                    pickle.dump(newrec,f1)                   
                    pickle.dump(l,f1)
        except: pass
    os.remove('employee details.dat')
    os.rename('Temp.dat','employee details.dat')
    print('Modified file:')
    with open('employee details.dat','rb') as f:
        try:
            while True:
                l=pickle.load(f)
                print(l)
        except:pass

def Del_Record():
    posname=input('Enter name to be deleted: ').capitalize()
    with open('employee details.dat','rb') as f, open('Temp.dat','wb') as f1:
        flag=0
        try:
            while True:
                l=pickle.load(f)
                if l[1]==posname:
                    pickle.dump(l,f1)
        except: pass
    os.remove('employee details.dat')
    os.rename('Temp.dat','employee details.dat')
    print('Modified file:')
    with open('employee details.dat','rb') as f:
        try:
            while True:
                l=pickle.load(f)
                print(l)
        except:pass


print('''MENU:
a. Create_Bin() - To create a binary file of (EnpId, EmpName, Designation )
b. Insert() : To insert before a particular record. (when name is given)
c. Del_Record() : To Delete a record when the name is given
d. Quit''')
while True:
    ch=int(input('Enter choice: '))
    if ch==1:
        n=int(input('Enter how many records: '))
        Create_Bin(n)
    elif ch==2:
        Insert()
    elif ch==3:
        Del_Record()
    elif ch==4:
        print('Exiting...')
        break
    else:
        print('invalid choice')

'''
MENU:
a. Create_Bin() - To create a binary file of (EnpId, EmpName, Designation )
b. Insert() : To insert before a particular record. (when name is given)
c. Del_Record() : To Delete a record when the name is given
d. Quit
Enter choice: 1
Enter how many records: 2
Enter employee id: 1
Enter employee name: kamlesh
Enter designation: ceo
Enter employee id: 2
Enter employee name: jayash
Enter designation: leader
File contents: 
[1, 'Kamlesh', 'Ceo']
[2, 'Jayash', 'Leader']
Enter choice: 3
Enter name to be deleted: jayash
Modified file:
[1, 'Kamlesh', 'Ceo']
Enter choice: 2
Before which record do you want to insert the new record: kamlesh
Enter new employee id: 2
Enter new employee name: arjun
Enter new designation: manager
Modified file:
[1, 'Kamlesh', 'Ceo']
Enter choice: 4
Exiting...
'''
