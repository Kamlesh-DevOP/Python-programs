pos,neg,zero=0,0,0
while True:
    n=int(input('Enter any number(-123 to stop): '))
    if n==-123:
        break
    
    if n>0:
        pos+=1
    elif n<0:
        neg+=1
    else:
        zero=+1
    
print('Positive-',pos,'Negative-',neg,'Zeroes-',zero)

    
