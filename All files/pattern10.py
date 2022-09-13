n=int(input('Enter number of rows: '))
m=1
for i in range(1,n+1):
    for k in range(1,2*i):
        print(m,end=' ')
        m+=1
    print()