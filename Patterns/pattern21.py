'''
*
**
***
****
*****
'''
n=5
for k in range(n):
    for j in range(k):
        print('',end='')
    for j in range(k,-1,-1):
        print('*',end='')
    print()