f=1
l=[]
x=int(input('Enter x: '))
n=int(input('Enter n: '))
for i in range(1,n+1):
    nr=x**i
    f*=i
    if i%2==0:
        l.append((nr/f)*-1)
    else:
        l.append(nr/f)
print(l)