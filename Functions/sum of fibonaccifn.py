def sum_fibnacci(n):
    a=-1
    b=1
    sum=0
    for i in range(n):
        c=a+b
        a=b
        b=c
        sum+=c
    return sum
a=int(input('Enter n: '))
print(sum_fibnacci(a))