'''
1/3!+1/5!+....1/n!
'''
n=int(input('Enter n: '))
sum=0
for i in range(3,n*2+2,2):
    print(i)
    for j in range(1,i+1):
        f*=j
    sum+=1/f
print(sum)
