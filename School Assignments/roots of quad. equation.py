print('Enter the coefficients of the quadratic equation you want to solve: ')
a=int(input('Enter value of a coefficient: '))
b=int(input('Enter value of b coefficient: '))
c=int(input('Enter value of c coefficient: '))
D=b**2-(4*a*c)
if D>0:
    print('Real roots')
    root1=(-b+D*(0.5))/2*a
    root2=(-b-D*(0.5))/2*a
    print(root1,'\t',root2)
elif D==0:
    print('Equal roots')
    root=(-b)/2*a
    print(root)
else: 
    print('Imaginary roots')
    root=(-b)/2*a,'+i',(D**0.5)/(2*a)
