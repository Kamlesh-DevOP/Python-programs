def Push():
    n=input('Enter country name: ').capitalize()
    m=input('Enter capital: ').capitalize()
    st.append([n,m])
def Pop():
    if st:
        print('Removed element:',st.pop())
    else:
        print('Underflow')
def Display():
    if st==[]:
        print('Empty stack')
    else:
        top=len(st)-1
        print(st[top],'<- top')
        for i in range(top-1,-1,-1):
            print(st[i])
def Peek():
    if st: print('Topmost element:',st[-1])
    else:print('Underflow')
st=[]
print('''MENU
1. Insert
2. Delete
3. Display Stack
4. Peek
5. Exit''')
while True:
    ch=int(input('Enter option: '))
    if ch==1: 
        Push()
    elif ch==2: 
        Pop()
    elif ch==3: 
        Display()
    elif ch==4: 
        Peek()
    elif ch==5:
        print('Exiting...')
        break
    else: 
        print('Invalid option')