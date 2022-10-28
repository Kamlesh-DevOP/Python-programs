n=int(input('Enter a decimal: '))
a=0
d=0
while n!=0:
    a+=((n%2)*(10**d))
    n//=2
    d+=1
print('Binary form is',a)