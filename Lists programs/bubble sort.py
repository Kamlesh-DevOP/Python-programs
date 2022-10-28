l=eval(input("Enter list: "))
for i in range(len(l)-1):
    for k in range(len(l)-i-1):
        if l[k]>l[k+1]:
            l[k],l[k+1]=l[k+1],l[k]
print(l)
