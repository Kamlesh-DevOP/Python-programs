digits=eval(input('Enter list of digits: '))
i=len(digits)-1
while digits[i]==9 and i>=0:
    digits[i]=0
    i-=1
if  i==-1:
    digits.insert(0,1)
else:
    digits[i]+=1
print(digits)
#wow
#looks simple but not really