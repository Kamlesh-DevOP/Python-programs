#wap to create a 2D matrix into a single list

l=[]
row=int(input('Enter rows: '))
col=int(input('Enter columns: '))
for i in range(row):
    l1=[]
    for j in range(col):
        l1+=[int(input('Enter elements: '))]
    l+=[l1]
for i in range(row):
    for j in range(col):
        print(l[i][j],end=' ')
    print()
ans=[]
for i in range(row):
    l1=[]
    for j in range(col):
        ans+=[l[i][j]]
print(ans)