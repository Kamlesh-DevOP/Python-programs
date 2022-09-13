f=float(input('Enter the first side of your triangle: '))
s=float(input('Enter the second side of your triangle: '))
t=float(input('Enter the third side of your triangle: '))
S=(f+s+t)/2
print('Area of triangle is ',(S*(S-f)*(S-s)*(S-t))**0.5 )
