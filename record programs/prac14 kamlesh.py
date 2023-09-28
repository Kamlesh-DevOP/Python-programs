import pickle,os
n=int(input('Enter number of employees: '))
with open('EMPLOYEE.dat','wb') as f:
    for i in range(n):
        name=input('Enter name: ').capitalize()
        age=int(input('Enter age: '))
        dept=input('Enter department: ').capitalize()
        desig=input('Enter designation: ').capitalize()
        sal=int(input('Enter salary: '))
        d={'Name':name,'Age':age,'Department':dept,'Designation':desig,'Salary':sal}
        pickle.dump(d,f)
print('''MENU
1. Display details of Managers earning more than 50000 in Finance and in Admin
Dept.
2. Delete the employee details who have reached retirement age(58 years)
3. Exit''')
while True:
    ch=int(input('Enter option: '))
    if ch==1:
        with open('EMPLOYEE.dat','rb') as f:
            flag=0
            try:
                while True:
                    d=pickle.load(f)
                    if d['Designation'].lower()=='manager' and d['Salary']>50000 and (d['Department'].lower() in ['admin','finance']):
                        print('Name:',d['Name'],'\tAge:',d['Age'],'\tDepartment:',d['Department'],'\nDesignation:',d['Designation'],'\tSalary:',d['Salary'])
                        flag=1
            except EOFError:
                if flag==0:
                    print('No match found')
    elif ch==2:
        with open('EMPLOYEE.dat','rb') as f, open('Temp.dat','wb') as f1:
            flag=0
            try:
                while True:
                    d=pickle.load(f)
                    if d['Age']<58:
                        pickle.dump(d,f1)
            except EOFError:pass
        os.remove('EMPLOYEE.dat')
        os.rename('Temp.dat','EMPLOYEE.dat')
        print('Modified file:')
        with open('EMPLOYEE.dat','rb') as f:
            try:
                while True:
                    d=pickle.load(f)
                    for i in d:
                        print(i,d[i],sep='-')
            except:pass
    elif ch==3:
        print('Exiting...')
        break
    else:
        print('Invalid option')

'''
Enter number of employees: 4
Enter name: kamlesh
Enter age: 42
Enter department: admin
Enter designation: manager
Enter salary: 60000
Enter name: amit
Enter age: 18
Enter department: finance
Enter designation: trainee
Enter salary: 40000
Enter name: jayash
Enter age: 59
Enter department: system
Enter designation: team leader
Enter salary: 70000
Enter name: arjun
Enter age: 41
Enter department: finance
Enter designation: manager
Enter salary: 60000
MENU
1. Display details of Managers earning more than 50000 in Finance and in Admin  
Dept.
2. Delete the employee details who have reached retirement age(58 years)        
3. Exit
Enter option: 1
Name: Kamlesh   Age: 42         Department: Admin
Designation: Manager    Salary: 60000
Name: Arjun     Age: 41         Department: Finance
Designation: Manager    Salary: 60000
Enter option: 2
Modified file:
Name - Kamlesh  
Age - 42        
Department - Admin
Designation - Manager
Salary - 60000
Name - Amit
Age - 18
Department - Finance
Designation - Trainee
Salary - 40000
Name - Arjun
Age - 41
Department - Finance
Designation - Manager
Salary - 60000
Enter option: 3
Exiting...
'''