'''
if input is 4, print
8 
8 6
8 6 4
8 6 4 2
'''
n=int(input('Enter n: '))
for i in range(n):
    for k in range(i+1):
        s=(n-k)*2
        print(s,end=' ')
    print()
#by Srishanth
#from Ajeetha