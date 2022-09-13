count, sum=0,0
for i in range(5,501):
    n=str(i)
    p=len(n)
    s=0
    for k in n:
        s+=int(k)**p
    if i==s:
        print(i, end=' ')
        sum+=i
        count+=1
print('Average of these numbers is',sum/count)
