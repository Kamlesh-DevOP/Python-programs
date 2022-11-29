row=int(input('Enter number of rows: '))
column=int(input('Enter number of columns '))
l=[]
for i in range(row):
    l1=[]
    for j in range(column):
        l1.append(int(input('Enter element: ')))
    l.append(l1)

for i in range(row):
    for j in range(column):
        print(l[i][j],end=' ')
    print() 
    
collist=[]
for i in range(row):
    collist+=[l[i][0]]
max_in_col=max(collist) #max_in_col is maximum element in first column

for i in range(row):
    for j in range(column):
        if l[i][0]==max_in_col:
            maxcolindex=i #maxcolindex is index of maximum element in 1st column
            
maxcol_rowlist=[] #maxcol_rowlist is rowlist of the maximum column
for i in range(column):
    maxcol_rowlist+=[l[maxcolindex][i]]

for i in range(len(maxcol_rowlist)):
    if l[maxcolindex][i]==min(maxcol_rowlist):
        minrowindex=i #index of minimum value in maxcol_rowlist
saddle=l[maxcolindex][minrowindex]
print(saddle,'is the saddle of this matrix found in',maxcolindex,minrowindex)