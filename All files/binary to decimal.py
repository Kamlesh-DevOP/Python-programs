n=int(input('Enter a binary number: '))
str=str(n)
s=0
i=0
while n!=0:
    r=n%10
    n=n//10
    dig=r*2**i
    s+=dig
    i+=1
print(s)
        