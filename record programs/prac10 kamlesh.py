import MATRIX as m
print('''MENU
1. Input the Matrix
2. Swap diagonals
3. Sort rows and columns
4. Exit''')
while True:
    ch=int(input('Enter option:'))
    if ch==1:
        n=int(input('Enter number of rows :'))
        l=[]
        for i in range(n):
            l1=[]
            for j in range(n):
                l1.append(int(input('Enter number:')))
            l.append(l1)
    elif ch==2:
        if l:
            m.SWAP(l)
        else:
            print('input matrix first')
    elif ch==3:
        m.SORTROWCOL(l)
    elif ch==4:
        print('Exiting...')
        break
    else:
        print('invalid option')