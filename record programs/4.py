def binarysearch(l,s):
    lower=0
    upper=len(l)-1
    l.sort()
    print(l)
    while lower<=upper:
        mid=(lower+upper)//2
        if l[mid]==s:
            return mid
        elif l[mid]>s:
            upper=mid-1
        elif l[mid]<s:
            lower=mid+1
def reverse_str(s):
    return s[::-1]
while True:
    print('''MENU
1. Binary search
2. Reverse a string
3. Exit''')
    ch=int(input('Enter choice: '))
    if ch==1:
        l=[]
        x=int(input("Enter the number of elements: "))
        for i in range(x):
            x1=int(input("Enter the number: "))
            l.append(x1)
        s=int(input("Enter number to search: "))
        r=binarysearch(l,s)
        print(s,'is present in',r+1,"position")
    elif ch==2:
        st=input('Enter string to reverse: ')
        print(reverse_str(st))

    elif ch==3:
        break
    else:
        print('Invalid option')
    print()