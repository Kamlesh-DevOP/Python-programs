d={}
n=int(input('Enter n: '))

for i in range(n):
    name=input('Enter name: ')
    no=int(input('Enter number: '))
    d[no]=name

while True:
    choice= int(input('Enter 1 to search for a number, 2 for displaying numbers in ascending order, 3 to quit: '))

    if choice==1:
        search=int(input('Enter number to be searched '))
        for i in d:
            if search==i:
                print(d[i])
        if search not in d:
            print('Number not found')
    
    elif choice==2:
        l=list(d.keys())
        l.sort()
        for i in l:
            print(d[i],end=' ')
        print()

    elif choice==3:
        break
    
    else:
        print('Invalid menu code')