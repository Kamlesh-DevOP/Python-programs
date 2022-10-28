l=eval(input('Enter a list: '))
sum=0
i=0
while i<len(l):
    if l[i]%2==0:
        sum+=l[i]
    i+=1
print(sum)