num=int(input('Enter 2 digit number: '))
u=num%10
t=num//10
reverse=u,t
actual=t,u
if reverse==actual:
    print('This number is a palindrome!', '\nCannot reverse this number')
else:
    print('The reverse of your number is: ', u,t, sep='')
