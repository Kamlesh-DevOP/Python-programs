start=int(input('Enter start number: '))
end=int(input('Enter end number number: '))
prime=[]
composite=[]
for j in range(start,end+1):
    for i in range(2,j):
        if j%i==0:
            composite.append(j)
            break
    else:
        prime.append(j)
print('Prime numbers are')
for x in prime:
    print(x)
print('Composite numbers are')
for x in composite:
    print(x)

