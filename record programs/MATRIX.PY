def SWAP(L):
    '''Swaps the primary and secondary diagonal of a nested list/matrix'''
    print('Original matrix: ')
    for i in range(len(L)):
        for j in range(len(L)):
            print(L[i][j], end=' ')
        print()
    for i in range(len(L)):
        for j in range(len(L)):
            if i==j:
                L[i][j],L[i][len(L)-1-j]=L[i][len(L)-1-j],L[i][j]
    print('Swapped matrix: ')
    for i in range(len(L)):
        for j in range(len(L)):
            print(L[i][j], end=' ')
        print()

def SORTROWCOL(actuallist):
    '''Sorts the rows of a matrix using bubble sort and columns using insertion sort individually'''
    L=actuallist.copy()
    print('Original matrix: ')
    for i in range(len(L)):
        for j in range(len(L)):
            print(L[i][j], end=' ')
        print()
    for l in range(len(L)):
        for i in range(len(L[l])-1):
            for k in range(len(L[l])-i-1):
                if L[l][k]>L[l][k+1]:
                    L[l][k],L[l][k+1]=L[l][k+1],L[l][k]            
    print('Row sorted matrix: ')    
    for i in range(len(L)):
        for j in range(len(L)):
            print(L[i][j], end=' ')
        print()
    L=actuallist.copy()
    print('Column sorted matrix:')
    for j in range(len(L)):
        for k in range(1,len(L)):
            key=L[k][j]
            x=k-1
            while x >= 0 and key <=L [x][j]:
                L[x+1][j]=L[x][j]
                x-=1
                L[x+1][j]=key
    for i in range(len(L)):
        for j in range(len(L)):
            print(L[i][j], end=' ')
        print()         
