#from Shaashu
n=int(input('Enter number 1: '))
m=int(input('Enter number 2: '))
for i in range(1,(n*m)+1):
    if n%i==0  and m%i==0:
        hcf=i
print(hcf)