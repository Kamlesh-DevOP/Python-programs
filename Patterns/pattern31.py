n=int(input('Enter number: '))
print(0,end=' ')
for i in range(0,n+1):
    if i==0:
        print()
    else:
        for j in range(0,(i**2)+1,i):
            print(j,end=' ')
        print()
'''
0 
0 1 
0 2 4 
0 3 6 9 
0 4 8 12 16 
0 5 10 15 20 25
'''