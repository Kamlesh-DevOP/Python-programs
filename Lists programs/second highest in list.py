l=eval(input('Enter list: '))
if l[0]>l[1]:
    max=l[0]
    sec_max=l[1]
else:
    max=l[0]
    sec_max=l[1]

for i in l[2:]:
    if i>max:
        sec_max=max
        max=i
    elif i>sec_max:
        sec_max=i
print(sec_max)

if l[0]>l[1]:
    min=l[1]
    sec_min=l[0]
else:
    min=l[0]
    sec_min=l[1]

for j in l[2:]:
    if j<min:
        sec_min=min
        min=j
    elif j<sec_min:
        sec_min=j
print(sec_min)