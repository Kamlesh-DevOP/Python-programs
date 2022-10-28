l=eval(input('Enter a list: '))
half=len(l)//2
j=-1
for i in range(half):
    l[i],l[j]=l[j],l[i]
    j-=1
print(l)

#Me and Gowtham did in cs lab
#I wrote the code he corrected the error