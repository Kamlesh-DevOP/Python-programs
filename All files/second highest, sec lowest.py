#Gowtham's method
l=eval(input('Enter list: '))
max=min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
sec_max=min
for i in l:
    if i>sec_max and i<max:
        sec_max=i
sec_min=max
for j in l:
    if j<sec_min and j>min:
        sec_min=j
print(sec_max,sec_min)