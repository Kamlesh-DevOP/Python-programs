u=int(input('Enter u: '))
sum,sign=0,-1
for i in range(1,6,2):
    nr=1
    dr=u**i
    sum+=(nr/dr)*sign
    sign*=-1
print(sum)