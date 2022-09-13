n=int(input('Enter your number: '))
s=0
while n!=0:
    r=n%10
    n=n//10
    s+=r
print(s)