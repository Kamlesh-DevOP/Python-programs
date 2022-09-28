str=input('Enter a 4 digit number')
rev=str[-1]+str[-2]+str[-3]+str[-4]
print('Reverse of your number is', rev)
if str==rev:
    print("You've entered a palindrome")
else:
    print('Not a palindrome!')