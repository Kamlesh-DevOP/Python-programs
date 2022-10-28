'''
1 
1 2 3
1 2 3 4 5
'''
n=int(input('Enter the number of terms: '))
for i in range(1,n*2+1):
    if i%2==1:
        for j in range(1,i+1):
            print(j,end=' ')
        print()
        