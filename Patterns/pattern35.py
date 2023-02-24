'''
1
1 3
1 3 6
1 3 6 9
'''
n=int(input('Enter n: '))
for i in range(3,n*3+1,3):
    print(1,end=' ')
    for j in range(3,i,3):
        print(j,end=' ')
    print()