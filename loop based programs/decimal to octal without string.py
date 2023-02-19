dec=int(input('enter decimal: '))
ans=0
i=0
while dec:
    dig=dec%8
    ans+=dig*10**i
    i+=1
    dec//=8
print(ans)