#single loop
l=eval(input('Enter list: '))
for i in range(len(l)):
    print(l[i][i],end=' ')
print()
#secondary loop
l=eval(input('Enter list: '))
for i in range(len(l)):
    for j in range(len(l)):
        if i==j:
            print(l[i][j],end=' ')