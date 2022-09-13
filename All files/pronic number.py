#pronic number is like 12=3*4 where 3 and 4 are consecutive numbers
num=int(input('Enter the number: '))
flag=0
for i in range(num):
    if i*(i+1)==num:
        flag=1
        break

if flag==1:
    print("It is a pronic number")
else:
    print('Not a pronic number')