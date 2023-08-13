def Fact(x):
    f = 1
    for i in range(2,x+1):
        f*=i
    return f

def fibo(n):
    f1 = -1
    f2 = 1
    for i in range(n):
        f3 = f1+f2
        print(f3,end=' ')
        f1 = f2
        f2 = f3

print( ''' Menu
1 - Generate factorial of a number
2 - Generate \'n\' numbers of Fibonacci series
3 - Exit''')

while True:
    ch = int(input('Enter a choice: '))
    if ch == 1:
        x= int(input('Enter Number to find Factorial: '))
        print(Fact(x))
    elif ch == 2:
        n = int(input('Enter Number of terms for fibonacci series: '))
        fibo(n)
        print()
    elif ch == 3:
        break
    else:
        print('Invalid option')
    print()