#from Shaashu
n=int(input('Enter number 1: '))
m=int(input('Enter number 2: '))
if n>m:
    p=m
    e=n
else:
    p=n
    e=m
for i in range(e,(n*m)+1):
    if i%n==0 and i%m==0:
        print(i)
        break