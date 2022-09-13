import math
a=int(input('Enter a: '))
b=int(input('Enter b: '))
c=int(input('Enter c: '))
if a==0:
    print('Invalid equation')
else:
    d=b**2-(4*a*c)
    sq=math.sqrt(abs(d))
    if d>0:
        print('Real and unequal roots')
        print((-b-sq)/(2*a))
        print((-b+sq)/(2*a))
    elif d==0:
        print('Real and equal roots')
        print(-b/(2*a))
    else:
        print('Imaginary roots')
        print(-b/(2*a),'+i',sq*(2*a))
        print(-b/(2*a),'-i',sq*(2*a))

        






