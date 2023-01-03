l=eval(input('Enter list: '))
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j],end=' ')
    print()
print('*'*50)
for i in range(len(l)):
    for j in range(len(l)):
        print(l[j][i],end=' ')
    print()