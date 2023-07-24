D=dict()
def add():
    phno=int(input('Enter phone number: '))
    name=input('Enter name: ')
    D[phno]=name
    print('Name added')
def view():
    for i in D:
        print(i, D[i])
def modify(phno):
    newname=input('Enter new name: ')
    if phno in D:
        D[phno]=newname
        print('Dictionary modified')
    else:
        print('Invalid phone number')
def delete(phno):
    if phno in D:
        for i in D:
            if phno==i:
                del D[phno]
                print('Phone number deleted')
                break
            
    else:
        print('Invalid phone number')

print('''MENU
1. ADD
2. VIEW
3. MODIFY NAME
4. DELETE
5. EXIT''')
while True: 
    ch=int(input('Enter choice: '))
    if ch==1:
        add()
    elif ch==2:
        view()
    elif ch==3:
        phno=int(input('Enter phone number to modify: '))
        modify(phno)
    elif ch==4:
        phno=int(input('Enter phone number to modify: '))
        delete(phno)
    elif ch==5:
        break
    else:
        print('Invalid choice')
