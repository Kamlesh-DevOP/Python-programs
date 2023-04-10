n=int(input('enter number: '))
bin=str(bin(n))
bin=bin[2:]
bin+='0'
max=0

c=0
for i in bin:
  if int(i)^0!=0:
    c+=1
  else:
     if max<c:
       max=c
       c=0
print(max)