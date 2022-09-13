#from Shaashu
n=int(input('Enter number 1: '))
m=int(input('Enter number 2: '))
for i in range(1,(n*m)+1):
    if i%n==0 and i%m==0:
        print(i)
        break