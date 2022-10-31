#2^n-1 in a list 
n=int(input('Enter n: '))
l=[]
for i in range(1,n+1):
    l.append(2**i-1)
print(l)