l=eval(input('Enter list: '))
s=0
for i in range(len(l)):
    for j in range(len(l)):
        if i==0 or j==0 or i==len(l)-1 or j==len(l)-1:
            print(l[i][j],end=' ')
            s+=l[i][j]
        else: print(' ',end=' ')
    print()