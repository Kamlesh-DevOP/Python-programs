#sum of 1!/2!+2!/4!+....
n=int(input('Enter the n: '))
x=int(input('Enter the x: '))
sum1=0
for i in range(1,n+1):
    nr=1
    for j in range(1,i+1):
        nr*=j
    dr=1
    for k in range(1,i*2+1):
        dr*=k
    sum1+=nr/dr
print(sum1)
