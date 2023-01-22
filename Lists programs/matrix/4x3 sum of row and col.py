L=eval(input("sales details for 3 salesperson in 4 quarter:"))
rowsum=[]
colsum=[]
print(' '*30,'Row Total')
print()
for i in range(3):
    sum=0
    for j in range(4):
        sum+= L[i][j]
    rowsum+= [sum]
for j in range(4):                  
    sum=0
    for i in range(3):        
        sum+=L[i][j]
    colsum +=[sum]
for i in range(3):
    print('Sales person '+str(i+1)+': ',end='')
    for j in range(4):
        print(L[i][j], end= "   ")
    print('  ',rowsum[i])
    print()
print('Column Total:   ',end='')
for k in colsum:
    print(k, end="  ")
