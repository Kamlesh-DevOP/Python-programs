'''
1        1
12      21
123    321
1234  4321
1234554321
'''
a=8
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print(' '*a,end='')
    a-=2
    for l in range(i,0,-1):
        print(l,end='')
    print()