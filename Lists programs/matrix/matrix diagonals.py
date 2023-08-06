l=eval(input('Enter matrix: '))
for i in range(len(l)):
    for j in range(len(l)):
        if i==j or i+j==len(l)-1:
            print(l[i][j],end=' ')
        else:
            print(' ',end=' ')
    print()