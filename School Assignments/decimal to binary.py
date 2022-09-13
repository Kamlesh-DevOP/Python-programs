n=int(input("Enter a number in decimal: "))
binary=''
while n!=0:
    r=n%2
    a=str(r)
    n=n//2
    binary=a+binary
print("The binary form of the number is",binary)
    