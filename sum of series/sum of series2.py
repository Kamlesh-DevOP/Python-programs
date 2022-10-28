#x/1!-x^2/3!+x^3/5!....
n=int(input('Enter the n: '))
x=int(input('Enter the x: '))
sum1,sign=0,1
for i in range(1,n+1):
    nr=x**n
    f=1
    for j in range(1,i*2):
        f=f*j
    sum1+=(nr/f)*sign
    sign*=-1
print(sum1)