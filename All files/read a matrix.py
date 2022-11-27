row=int(input('Enter row: '))
column=int(input('Enter column: '))
l=[]
for i in range(row):
    l1=[]
    for j in range(column):
        l1.append(int(input('Enter element: ')))
    l.append(l1)
print(l)
for i in range(row):
    for j in range(column):
        print(l[i][j],end=' ')
    print()
