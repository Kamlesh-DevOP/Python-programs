l=eval(input('Enter list: '))
for i in range(len(l)):
    for j in range(0,len(l),2):
        print(l[i][j],end=' ')
    print()
