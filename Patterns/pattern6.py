'''
1#
2*2*
3#3#3#...
'''
n=int(input('Enter number of lines: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2==1:
            print(i,end='#')
        if i%2==0:
            print(i,end='*')
    print()

        