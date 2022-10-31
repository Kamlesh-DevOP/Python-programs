flag=0
l=eval(input('Enter a list: '))
while True:
    n=input('What element do you want to find?')
    for i in l:
        if i==n:
            flag=1
    if flag==1:
        print(n,'is present in this list')
    else:
        print(n,'is not present in this list')
        #incomplete
