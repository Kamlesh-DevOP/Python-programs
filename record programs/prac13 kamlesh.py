import pickle
with open('STUDENT.dat','wb') as f:
    N=int(input('Enter number of students: '))
    for i in range(N):
        rno=int(input('Enter roll number: '))    
        name=input('Enter name: ')
        stream=input('Enter stream: ')
        total=int(input('Enter total: '))
        l=[rno,name,stream,total]
        pickle.dump(l,f)
    print('File created successfully')
while True:
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
                mx=mx1=mx2=mx3=0
                while True:
                    l=pickle.load(f)
                    if l[2].lower()=='computer science':
                        if l[3]>mx:
                            mx=l[3]
                            det=l
                    if l[2].lower()=='biology':
                        if l[3]>mx1:
                            mx1=l[3]
                            det1=l
                    if l[2].lower()=='commerce':
                        if l[3]>mx2:
                            mx2=l[3]
                            det2=l
                    if l[2].lower()=='eg':
                        if l[3]>mx3:
                            mx3=l[3]
                            det3=l
            except EOFError:
                    pass
        print('Computer science topper:',det)
        print('Biology topper:',det1)
        print('Commerce topper:',det2)
        print('EG topper:',det3)
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
                    print(l)
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
Enter name: avaneesh
Enter stream: biology
Enter total: 456
Enter roll number: 3
Enter name: jayash
Enter stream: commerce
Enter total: 489
Enter roll number: 4
Enter name: kamlesh
Enter stream: computer science
Enter total: 490
Enter roll number: 5
Enter name: vignesh
Enter stream: eg
Enter total: 487
File created successfully
MENU
1. Display Stream wise topper detail
2. Increment the total by 3 marks for students in the biology stream and decrement by 2 for
students in EG stream.
3. Exit
Enter choice: 1
Computer science topper: [4, 'kamlesh', 'computer science', 490]
Biology topper: [2, 'avaneesh', 'biology', 456]
Commerce topper: [3, 'jayash', 'commerce', 489]
EG topper: [5, 'vignesh', 'eg', 487]
MENU
1. Display Stream wise topper detail
2. Increment the total by 3 marks for students in the biology stream and decrement by 2 for
students in EG stream.
3. Exit
Enter choice: 2
Marks modified
[1, 'arjun', 'computer science', 485]
[2, 'avaneesh', 'biology', 459]
[3, 'jayash', 'commerce', 489]
[4, 'kamlesh', 'computer science', 490]
[5, 'vignesh', 'eg', 485]
MENU
1. Display Stream wise topper detail
2. Increment the total by 3 marks for students in the biology stream and decrement by 2 for
students in EG stream.
3. Exit
Enter choice: 3
Exiting...
'''