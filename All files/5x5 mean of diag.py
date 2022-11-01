#find mean of diagonal elements excluding centre element
l=eval(input('Enter list: '))
sum=0
count=0
for i in range(5):
    for j in range(5):
        if ((i==0 or i==4) and (j==0 or j==4)) or ((i==1 or i==3) and (j==1 or j==3)):
            print(l[i][j],end=' ')
            sum+=l[i][j]
            count+=1
        else: print(' ', end=' ')
    print()
print('mean: ',sum/count)