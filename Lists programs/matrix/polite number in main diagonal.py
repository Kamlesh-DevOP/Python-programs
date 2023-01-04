l=[]
for i in range(4):
    l1=[]
    for j in range(4):
        l1+=[int(input('Enter elements: '))]
    l+=[l1]

for i in range(4):
    for j in range(4):
        print(l[i][j],end=' ')
    print()

print('polite numbers') #polite numbers are eeverything other than powers of 2
for i in range(4):
    for j in range(4):
        if i==j:
            k=1
            while 2**k<=l[i][j]:
                k+=1
            if 2**(k-1)!=l[i][j]:
                print(l[i][j],end=' ')