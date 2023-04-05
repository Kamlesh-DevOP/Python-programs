def primecheck(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input('Enter number: '))

if primecheck(n):
    print(n,'is a prime number')
else:
    print(n,'is not a prime number')
