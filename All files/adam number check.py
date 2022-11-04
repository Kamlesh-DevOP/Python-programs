#12 is an adam no. because 12^2 is reverse of 21^2
n=int(input('Enter any number: '))
rev=int(str(n)[::-1])
if n**2==int(str(rev**2)[::-1]):
    print(n,'is an adam number')  
else:
    print('Not an adam number')  

