'''
4 3 2 1 
4 3 2 
4 3 
4 
'''
n=int(input('Enter the number: '))
for k in range(n):
    for j in range(n,k,-1):
        print(j,end=' ')
    print()