n=int(input('Enter any number: '))
rev=0
while n!=0:
    d=n%10
    n=n//10
    rev=rev*10+d
print(rev)  