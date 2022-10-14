l=eval(input('Enter a list: '))
half=int(len(l)/2)
for i in range(half):
    l[i],l[half+i]=l[half+i],l[i]
print(l)