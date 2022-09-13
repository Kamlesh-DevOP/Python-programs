#1+ 1^2+ 2^2+ 1^3+ 2^3+ 3^3
n=int(input('Enter the n: '))
s=0
for i in range(1,n+1):
    for j in range(1,i+1):
        s+=j**i
print(s)

