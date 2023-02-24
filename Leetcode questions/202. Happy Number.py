s=int(input('Enter number: '))
l=set() #i used set becuase sets are unordered and have O(1) time complexity while list has O(n). also, sets are the best to use if searching something is more important
# i got 11ms more speed once i used set!!
while s!=1: 
    s=str(s)
    sum=0
    for i in s:
        sum+=int(i)**2
    s=sum

    if s in l:
        print('False')
    l.add(s)
print('True')
 ##jayash orz orz