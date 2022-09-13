ask=input('Using for loop or while loop? ')
a=int(input('How many times to repeat? '))
b=input('What to repeat? ')
if ask=='while':
    i=0
    while i<a:
        print(b)
        i+=1
elif ask=='for':
    for i in range(a):
        print(b)