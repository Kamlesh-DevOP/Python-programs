l=eval(input('Enter matrix: '))
for i in range(len(l)):
    for j in range(len(l)):
        if i==j or i==3-j-1:
            print(l[i][j],end=' ')
        else:
            print(' ',end=' ')
    print()