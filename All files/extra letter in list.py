'''
1. Write a program in Python that accepts two string parameters. The first parameter will be
a string of characters, and the second parameter will be the same string of characters,
but they’ll be in a different order and have one extra character. The function should
return that extra character.
For example, if the first parameter is “eueiieo” and the second is “iieoedue,” then the
function should return “d.”
'''

#Code:
str1=input('Enter string 1: ')
str2=input('Enter string 2: ')
lst1=list(str1)
lst2=list(str2)
i=0
if len(lst1)!=len(lst2):
    while i<=len(lst1):
        j=i=0
        while j<len(lst2):
            if lst1[i]==lst2[j]:
                lst1.pop(i)
                lst2.pop(j)
            j+=1
        i+=1
    if len(lst2)==1:
        print(lst2[0])
else:
    print('There is an error in the given input. Please check it')
    

#Outputs:
'''
Enter string 1: eueiieo
Enter string 2: iieoedue
d

Enter string 1: aaaa
Enter string 2: aaaaa
a

Enter string 1: reverse
Enter string 2: desrever
d
'''
#class 11 annual practicals program 1