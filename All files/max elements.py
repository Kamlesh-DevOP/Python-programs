'''
Write a program which accepts a list of integers and stores the
element(s) which is(are) present maximum number of times in a new
list and prints the resultant list /error message .
Eg1. If the original list is [ 4,3,5,4,1,3,6,4,4,3,2,4]
Then the new list will be [4].
Eg2. If the original list is [4,3,4,5,6,3,7]
Then the new list will be [4,3].
Eg3. If the original list is [3,4,5,6,7]
The new list will be [3,4,5,6,7]

'''


l=eval(input('Enter list: '))
c=0
a=[]
for k in l:
    m=l.count(k)
    if m>c:
        c=m
for k in l:
    if c==l.count(k) and k not in a:
        a.append(k)
print(a)

#Madhu the genius