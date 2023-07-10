from random import *

x=int(input('enter x: '))
y=int(input('enter y: '))
n=int(input('Enter number of numbers to be generated: '))
if n>y-x:
    print('not possible')
else:
    l=[]
    for i in range(n):
        l+=[randint(x,y)]
    print(l)
    l=list(set(l))


def largest(l):
    l.sort()
    return l[-1]

def secondlargest(l):
    l.sort()
    return l[-2]

def primeinlist(l):
    for i in l:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=' ')
    print()
c='y'
while c=='y':
    print('''press 1 for largest number
    2 for 2nd largest number
    3 for finding all the prime numbers''')
    ch=int(input('enter your choice: '))
    if ch==1:
        print(largest(l))
    elif ch==2:
        print(secondlargest(l))
    elif ch==3:
        primeinlist(l)
    else:
        print('wrong option')
    c=input('do you want to continue(y/n): ')


