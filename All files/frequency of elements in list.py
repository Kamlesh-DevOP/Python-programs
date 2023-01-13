d={}
l=eval(input('Enter a list (with repetitive elements): '))
for i in l:
    if i not in d:
        d[i]=l.count(i)
print(d)