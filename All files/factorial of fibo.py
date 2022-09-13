n=int(input('How many values? '))
a=-1
b=1
for i in range(n):
    c = a + b
    a = b
    b = c
    f=1
    for j in range(1,c+1):
        f*=j
    print(c,f)