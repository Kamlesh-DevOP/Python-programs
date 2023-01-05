#convert strings in list to nested list
l=eval(input('Enter list: '))
l1=[]
for i in l:
    temp=[]
    temp.append(i)
    l1.append(temp)
print(l1)
#if input is ['abc','cde',4,6.7]
#op is [['abc'], ['cde'], [4], [6.7]]