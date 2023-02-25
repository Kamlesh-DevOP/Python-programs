'''
1
3 1
1 3 5
7 5 3 1
1 3 5 7 9
'''
n=int(input('Enter n: '))
c=0
for i in range(1,n):
    if c%2==0:
        for j in range(1,i*2,2):
            print(j,end=' ')
    else:
        for k in range(i*2-1,0,-2):
            print(k,end=' ')
    print()
    c+=1