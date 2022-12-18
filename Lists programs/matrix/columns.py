l=eval(input('Enter matrix: '))
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j],end=' ')
    print()
print('**********************************')
for k in range(len(l)):
    for m in range(len(l)):
        print(l[m][k])
    if k!=len(l)-1:
        print('next col')

