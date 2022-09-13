n=int(input('How many values? '))
a=-1
b=1
count=0
for i in range(n):
    c = a + b
    print(c,end=' ')
    if c>1:
        for j in range(2,c):
            if c%j==0:
                break
        else:
            count+=1
    a=b
    b=c
print('\n',count,'Prime numbers')