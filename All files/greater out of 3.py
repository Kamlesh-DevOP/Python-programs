x=int(input('Enter first number: '))
y=int(input('Enter second number: '))
z=int(input('Enter third number: '))
if x>y:
    if x>z:
        print(x,'is greatest')
    else:
        print(z,'is greatest')
elif y>x:
    if y>z:
        print(y,'is greatest')
    else: 
        print(z,'is greatest')
else:
    print('All numbers are equal')

