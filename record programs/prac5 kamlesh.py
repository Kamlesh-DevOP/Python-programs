from random import randint
l=[]
def Generate(ll,ul):
    global l
    l=[]
    for i in range(5):
        l.append(randint(ll,ul))
    return l

def Max_SecMax():
    max=secmax=0
    for i in l:
        if i>max:
            secmax=max
            max=i
        if i<max and i>secmax:
            secmax=i
    return max,secmax

def Prime():
    lolist=[]
    for i in l:
        if i>=2:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                if i not in lolist:
                    lolist.append(i)
    if lolist:
        return lolist
    else:
        return 'no prime numbers in the generated list'

print('''MENU:
1. Generate list of 5 random numbers
2. Print highest and second highest numbers from the generated list
3. Print the prime numbers from the generated list
4. Exit''')
while True:
    ch=int(input('Enter a menu code: '))
    if ch==1:
        ul=int(input('Enter upper limit: '))
        ll=int(input('Enter lower limit: '))        
        print(Generate(ll,ul))
    elif ch==2:
        print(Max_SecMax()[0],'is the highest',Max_SecMax()[1],'is the second highest')
    elif ch==3:
        print(Prime())
    elif ch==4:
        break
    else:
        print('Invalid option')
