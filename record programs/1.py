def Factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
 
def Power(x,p):
    return x**p

s1=0
sign=1
x=int(input('Enter x: '))
n=int(input('Enter n: '))
for i in range(1,n+1):
    s1+=Power(x,2*i-1)/Factorial(2*i)*sign
    sign*=-1
print(round(s1,2))
s2=0
sign=1
for i in range(1,n+1):
    s2+=Power(x,2*i-1)/Factorial(2*i+1)*sign
    sign*=-1
print(round(s2,2))