#1/1 + 1/2^2 + 1/3^2 + 1/4^2 + ..+1/n^2
n=int(input('Enter end value: '))
sum=0
for i in range(1,n+1):
    m=1/(i**2)
    sum+=m
print(sum)