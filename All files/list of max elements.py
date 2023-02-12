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

l=eval(input('enter list: '))
a=[]
max_count=0
for i in l:
    count=l.count(i)
    if count>max_count:
        max_count=count
for j in l:
    if l.count(j)==max_count:
        if j not in a:
            a.append(j)
print(a)
#madhu supremacy
#she did it in 10 mins whilw it took me more than 30 mins yet i failed :(