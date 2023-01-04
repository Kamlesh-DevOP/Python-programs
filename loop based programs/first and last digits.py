#print the sum of first and last number in a multiple digit number
n=int(input('Enter:'))
last=n%10
while n>=1:
    r=n%10
    n//=10
print('Sum of first and last digits of ',n,'is',r+last)