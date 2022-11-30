#arjun
'''
1A$
12B%
123C$
'''
n=int(input('Enter n: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print(chr(64+i),end='')
    print('$',end='')
    print()