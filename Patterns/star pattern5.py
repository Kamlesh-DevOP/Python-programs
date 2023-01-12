n=int(input('Enter n: '))
for i in range(0,n):
    for j in range(0,i):
        print(' ',end='')
    for k in range(i+1,n+1):
        print('*',end='')
    for l in range(i,n-1):
        print('*',end='')
    print()
'''  
*********
 *******
  *****
   ***
    *
'''
#hari supremacy