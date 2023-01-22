import random
l=[]
checker=[]
for i in range(5):
    l1=[]
    while len(l1)<5:
        a=random.randint(1, 25)
        if a not in checker:
            l1+=[a]
            checker+=[a]
    l+=[l1]
print(l)