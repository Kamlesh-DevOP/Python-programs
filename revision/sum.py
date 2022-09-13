x=int(input('Enter x: '))
sum,sign=0,1
for i in range(1,4):
    nr=x**i
    dr=1
    for j in range(1,i+1):
        dr*=j
    sum+=(nr/dr)*sign
    sign*=-1
print(sum)