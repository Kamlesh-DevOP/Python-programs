import random
l=[]
for i in range(5):
    x=random.randint(1,100)
    l.append(x)
print(l)
print('Sum: ',sum(l))
print('Mean: ',sum(l)/len(l))