import pickle
with open('STUDENT.dat','wb') as f:
    N=int(input('Enter number of students: '))
    for i in range(N):
        rno=int(input('Enter roll number: '))    
        name=input('Enter name: ').capitalize()
        stream=input('Enter stream: ').capitalize()
        total=int(input('Enter total: '))
        l=[rno,name,stream,total]
        pickle.dump(l,f)
    print('File created successfully')
    print('''MENU
1. Display Stream wise topper detail
2. Increment the total by 3 marks for students in the biology stream and decrement by 2 for
students in EG stream.
3. Exit''')
while True:
    ch=int(input('Enter choice: '))
    if ch==1:
        with open('STUDENT.dat','rb') as f:
            try:
                det=det1=det2=det3=None
                mx=mx1=mx2=mx3=0
                while True:
                    l=pickle.load(f)
                    if l[2].lower()=='computer science':
                        if l[3]>mx:
                            det=l
                    elif l[2].lower()=='biology':
                        if l[3]>mx1:
                            det1=l
                    elif l[2].lower()=='commerce':
                        if l[3]>mx2:
                            det2=l
                    elif l[2].lower()=='eg':
                        if l[3]>mx3:
                            det3=l
            except EOFError:
                    pass
        if det:
            print('Computer science topper:',det[1],'-',det[-1])
        if det1:
            print('Biology topper:',det1[1],'-',det1[-1])
        if det2:
            print('Commerce topper:',det2[1],'-',det2[-1])
        if det3:
            print('EG topper:',det3[1],'-',det3[-1])
    elif ch==2:
        with open('STUDENT.dat','rb+') as f:
            try:
                while True:
                    s=f.tell()
                    l=pickle.load(f)
                    if l[2].lower()=='biology':
                        l[3]+=3
                    elif l[2].lower()=='eg':
                        l[3]-=2
                    f.seek(s)
                    pickle.dump(l,f)
            except EOFError:
                pass
        print('Marks modified')
        with open('STUDENT.dat','rb+') as f:
            try:
                while True:
                    l=pickle.load(f)
                    if l[2] in ['Biology','EG']:
                        print(l[1],l[2],l[3])
            except:pass
    elif ch==3:
        print('Exiting...')
        break
    else:
        print('Invalid input')

'''
Enter number of students: 5
Enter roll number: 1
Enter name: arjun
Enter stream: computer science
Enter total: 485
Enter roll number: 2
Enter name: bala
Enter stream: commerce
Enter total: 499
Enter roll number: 3
Enter name: kamlesh
Enter stream: computer science
Enter total: 499
Enter roll number: 4
Enter name: mukund
Enter stream: eg
Enter total: 497
Enter roll number: 5 
Enter name: pravin
Enter stream: biology
Enter total: 489
File created successfully
MENU
1. Display Stream wise topper detail
2. Increment the total by 3 marks for students in the biology stream and decrement by 2 for
students in EG stream.
3. Exit
Enter choice: 1
Computer science topper: Kamlesh - 499
Biology topper: Pravin - 489
Commerce topper: Bala - 499
EG topper: Mukund - 497
Enter choice: 2
Marks modified
Pravin Biology 492
Enter choice: 3
Exiting...
'''