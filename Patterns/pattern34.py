'''
0
0 1
0 2 4
0 3 6 9
0 4 8 12 16
'''
n=int(input('Enter n: '))
for i in range(1,n+1):
    print(0,end=' ')
    if i!=0:
        for j in range(i,i*i+1,i):
            print(j,end=' ')
        print()
