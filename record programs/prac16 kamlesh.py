def Push(n):
    stk.append(n)
    top=len(stk)-1
def Pop(n):
    if stk==[]:
        return 'Underflow'
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def Display_Stack():
    if stk==[]:
        print('Empty stack')
    else:
        top=len(stk)-1
        print(stk[top],'<- top')
        for i in range(top-1,-1,-1):
            print(stk[i])
def Peek():
    if stk==[]:
        print('Underflow')
    else:
        top=len(stk)-1
        return stk[top]

stk=[]
top=None
print('''MENU
1. Push
2. Pop
3. Display Stack
4. Peek
5. Exit''')
while True:
    ch=int(input('Enter menu: '))
    if ch==1:
        item=int(input('Enter item: '))
        Push(item)
    elif ch==2:
        item=Pop(stk)
        if item=='Underflow':
            print('Underflow')
        else:
            print('Popped item is: ',item)
    elif ch==3:
        Display_Stack()
    elif ch==4:
        item=Peek()
        if item=='Underflow':
            print('Underflow')
        else:
            print('Topmost item is: ',item)
    elif ch==5:
        print('Exiting...')
        break
    else:
        print('Invalid option')

'''
Sample output
MENU
1. Push
2. Pop
3. Display Stack
4. Peek
5. Exit
Enter menu: 1
Enter item: 5
Enter menu: 1
Enter item: 7
Enter menu: 1
Enter item: 10
Enter menu: 2
Popped item is:  10
Enter menu: 2      
Popped item is:  7
Enter menu: 2     
Popped item is:  5
Enter menu: 2     
Underflow   
Enter menu: 1
Enter item: 7
Enter menu: 3
7 <- top    
Enter menu: 1
Enter item: 3 
Enter menu: 3
3 <- top    
7
Enter menu: 4
Topmost item is:  3
Enter menu: 6      
Invalid option
Enter menu: 5 
Exiting...
'''