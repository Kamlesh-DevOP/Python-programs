n=int(input('Enter n: '))
s=0
for i in range(n*2+1):
    if i%2==0:
        s+=i
print(s)
