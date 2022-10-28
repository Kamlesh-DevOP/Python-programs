n=int(input('Enter n: '))
a=-1
b=1
for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    for j in range(2,b):
        if b%j==0:
            break
    else:
        if b>1 and b<=n:
            print(b,end=' ')
            