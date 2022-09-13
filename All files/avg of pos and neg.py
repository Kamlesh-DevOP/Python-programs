pos,neg,zero=0,0,0
sumofpos=0
sumofneg=0
countofpos=0
countofneg=0
while True:
    n=int(input('Enter any number(-123 to stop): '))
    if n==-123:
        break
    if n>0:
        sumofpos+=n
        countofpos+=1
    if n<0:
        sumofneg+=n
        countofneg+=1

avgpos=sumofpos/countofpos
avgneg=sumofneg/countofneg
print('Average of positive numbers is',avgpos,'\nAverage of negative numbers is',avgneg)
