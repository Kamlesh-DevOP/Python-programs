m1=eval(input('Enter matrix 1: '))
m2=eval(input('Enter matrix 2: '))
sum_matrix=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1)):
        sum_matrix[i][j]=m1[i][j]+m2[i][j]
for i in range(len(m1)):
    for j in range(len(m1)):
        print(sum_matrix[i][j],end='  ')
    print()