'''
y**1/x**1! + y**3/x**2! + y**5/x**3!
'''
y=int(input('Enter y: '))
x=int(input('Enter x: '))
n=int(input('Enter n: '))
sum1=0
sign=1
for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
        f*=j
    for k in range(1,i*2,2):
        yp=k
    nr=y**yp
    dr=x**f
    sum1+=(nr/dr)*sign
    sign*=-1
print(sum1)



    