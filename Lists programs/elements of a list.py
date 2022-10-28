l=eval(input('Enter a list: '))
last=-len(l)
for i in range(len(l)):
    print(l[i],i,last)
    last+=1