#convert a string of lists into a nested list
'''
Example: 
Enter string of lists: '[[1,2,3],[4,5,6]' 
>>>[[1, 2, 3], [4, 5, 6]]'''
str=input('Enter string of lists: ')
list=[]
end=0
for i in range(end,len(str)):
    if (str[i]=='[' or str[i]==',') and str[i+1]=='[':
        temp=[]
        i+=2
        while str[i]!=']':
            if str[i]==',':
                i+=1
            else:
                temp+=[int(str[i])]
                i+=1
        end=i
        list.append(temp)
print(list)
#very proud of myself. it took me 2 days to figure this out. writing in paper actually works!!
#wow