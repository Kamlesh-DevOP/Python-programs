l=eval(input('Enter list: '))
count=0
for n in l:    
    rev=int(str(n)[::-1])
    sq_rev=int(str(rev**2)[::-1])
    if n**2==sq_rev:
        count+=1
print(count)