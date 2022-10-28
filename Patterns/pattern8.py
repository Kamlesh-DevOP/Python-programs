'''
if input is 4, print
8 6 4 2
8 6 4 
8 6
8
'''
n=int(input('Enter the number: '))
for k in range(n):
    for j in range(n,k,-1):
        print(j*2,end=' ')
    print()
#from Ajeetha