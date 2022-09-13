n=int(input('Enter decimal number: '))
octal=''
while n!=0:
    r=n%8
    a=str(r)
    n=n//8
    octal=a+octal
print("The octal form of the number is",octal)
