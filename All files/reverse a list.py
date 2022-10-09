rev=[]
l=eval(input('Enter a list: '))
for i in range(1,len(l)+1):
    rev.append(l[-i])
print(rev)