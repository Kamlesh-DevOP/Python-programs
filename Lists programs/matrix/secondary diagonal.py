l=eval(input('Enter the elements '))
x=[]
prime=[]
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            x.append(l[i][j])
for k in x:
    if k==0 or k==1:
        continue
    for t in range(2,k):
        if k%t==0:
            break
    else:
        if k not in prime:
            prime.append(k)
print(prime)
#mohnish and me