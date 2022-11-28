l=eval(input('Enter matrix: '))
for i in range(len(l)):
    for j in range(len(l)):
        k=len(l)-1
        if i==j:
            l[i][j],l[i][k-j]=l[i][k-j],l[i][j]
        k-=1
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j],end=' ')
    print()

