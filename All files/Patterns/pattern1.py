'''
1
12
123
1234
'''
n=int(input('Enter the number of terms: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()