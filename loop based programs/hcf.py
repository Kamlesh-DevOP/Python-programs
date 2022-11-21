#from Shaashu
n=int(input('Enter number 1: '))
m=int(input('Enter number 2: '))
if n>m:
    p=m
else:
    p=n
for i in range(1,(p)+1):
    if n%i==0  and m%i==0: #checks if both are divisible by a number from 1 to smaller number
        hcf=i 
print(hcf)