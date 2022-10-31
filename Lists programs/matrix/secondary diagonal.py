#nested loop
l=eval(input('Enter list: '))
for i in range(3):
    for j in range(2,-1,-1):
        print(l[i][j], end=' ')
    print()