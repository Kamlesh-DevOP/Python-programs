def FIND(lst):
    for i in range(len(lst)):
        max=0
        for j in range(len(lst[i])):
            if lst[i][j]>max:
                max=lst[i][j]
        lst[i]=max
    return lst

l=eval(input('Enter nested list: '))
print(FIND(l))
#got in first try!