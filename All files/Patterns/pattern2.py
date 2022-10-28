'''
1
22
333
4444
55555
'''
n=int(input('Enter the number of terms: '))
for i in range(1,n+1):
    for k in range(1,i+1):
        print(i,end='')
    print()