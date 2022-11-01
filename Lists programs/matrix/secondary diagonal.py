#nested loop
l=eval(input('Enter list: '))
for i in range(3):
    for j in range(2,-1,-1):
        if i+j==2:
            print(l[i][j], end=' ')
        else: print('  ', end=' ')
    print()
#single loop
for i in range(3):
    print(l[i][2-i],end=' ')