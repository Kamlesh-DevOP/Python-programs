num=int(input('Enter number: '))
s=str(num)
while len(s)!=1:
    sum=0
    for i in s:
        sum+=int(i)
    s=str(sum)
print(int(s))