#nested loop
l=eval(input('Enter list: '))
for i in range(len(l)):
    for j in range(len(l)):
        if i+j==len(l)-1:
            print(l[i][j], end=' ')
        else: print('  ', end=' ')
    print()
#single loop
for i in range(len(l)):
    print(l[i][len(l)-1-i],end=' ')