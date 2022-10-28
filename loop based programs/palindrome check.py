n=int(input('Enter a number: '))
num=n
rev=0
while n!=0:
    r=n%10
    d=n//10
    rev=rev*10+r
    n=d
if rev==num:
    print('It is a palindrome')
else: 
    print('It is not a palindrome')
