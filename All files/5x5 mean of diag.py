#find mean of diagonal elements excluding centre element
l=eval(input('Enter list: '))
sum=0
count=0
for i in range(5):
    for j in range(5):
        if (i==j or i+j==4) and not i==j==2 :
            print(l[i][j],end=' ')
            sum+=l[i][j]
            count+=1
        else: print(' ', end=' ')
    print()
print('mean: ',sum/count)