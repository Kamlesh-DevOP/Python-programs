def addup(l,n):
    for i in range(n):
        if i%2==0:
            l[i]+=l[i+1]
        else:
            l[i]+=10

l=[23,4,25,36,1,2]
n=6
addup(l,n)
print(l)