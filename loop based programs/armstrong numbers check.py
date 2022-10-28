n=int(input('Enter any number: '))
s=0
for i in str(n):
    p=len(str(n))
    s+=int(i)**p
    if s==n:
        print(n,'is an armstrong number!')
