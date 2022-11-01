l=eval(input('Enter list: '))
prime=[]
for i in l:
    for j in i:
        for k in range(2,j):
            if j%k==0:
                break
        else: 
            if j not in prime:
                prime.append(j)
for p in prime: 
    print(p,end=' ')

        