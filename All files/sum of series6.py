#1/1+1/2+1/3+1/4+..+n
n=int(input('Enter end value: '))
sum=0
for i in range(1,n+1):
    m=1/i
    sum+=m
print(sum)