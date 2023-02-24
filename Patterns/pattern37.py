'''
*
* *
* * *
* *
*
'''
n=int(input('Enter n: '))
for i in range(1,n+1):
    if i<=n//2+1:
        for j in range(1,i+1):
            print('*',end=' ')
    else:
        for k in range(i,n+1):
            print('*',end=' ')
    #for k in range():
    print()