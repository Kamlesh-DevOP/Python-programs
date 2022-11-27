'''
    1
   12
  123
 1234
12345
'''
space=4
for i in range(1,6):
    print(' '*space,end='')
    for j in range(1,i+1):
        print(j,end='')
    space-=1
    print()