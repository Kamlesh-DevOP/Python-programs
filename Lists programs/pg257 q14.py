l=eval(input('Enter list: '))
val=input('Enter alphabet to be searched: ')
for i in l:
    if i[0]==val:
        print(i, end=' ')