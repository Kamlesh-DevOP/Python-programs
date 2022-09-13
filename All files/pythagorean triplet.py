#from Shaashu
while True:
    i=int(input('Enter a number: '))
    j=int(input('Enter a number: '))
    k=int(input('Enter a number: '))
    if i>j and i>k:
        if i**2==j**2+k**2:
            print('Pythagorean Triplet')
        else: print('Not a triplet')    
    elif j>k and j>i:
        if j**2==k**2+i**2:
            print('Pythagorean Triplet')
        else: print('Not a triplet')    
    else:
        if k**2==i**2+j**2:        
            print('Pythagorean Triplet')
        else: print('Not a triplet')    
    if i==-1:
        break

