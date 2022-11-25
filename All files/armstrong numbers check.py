n=int(input('Enter any number: '))
s=0
p=len(str(n))
for i in str(n):
    s+=int(i)**p
if s==n:
    print(n,'is an armstrong number!')
else:
    print(n,'is not an armstrong number')