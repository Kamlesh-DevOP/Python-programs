'''
1
234
56789'''
n=int(input('Enter a number: '))
m=1
i=1
while i<=n:
    k=1
    while k<2*i:
        print(m,end=' ')
        m+=1
        k+=1
    i+=1
    print()