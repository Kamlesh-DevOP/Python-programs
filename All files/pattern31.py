n=int(input('Enter number: '))
print(0,end=' ')
for i in range(0,n+1):
    if i==0:
        print()
    else:
        for j in range(0,i**2+1,i):
            print(j,end=' ')
        print()