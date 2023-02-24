''' 
* 
* *
*   *
* *
*
'''
n=5
mid=n//2
for i in range(1,n+1):
    if i<mid+1:
        for j in range(1,i+1):
            print('*',end=' ')
        print()
    elif i==mid+1:
        print('*',(i-2)*' ','*')
    else:
        for k in range(n+1-i):
            print('*',end=' ')
        print()
