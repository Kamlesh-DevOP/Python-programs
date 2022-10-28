lst=eval(input('Enter a list: '))
i=0
lst+=['']
while i < len(lst):
    if lst[i]==0:
        del lst[i]
        lst.append(0)
        i-=1            #to restart the next loop from the same place which got completed
    i+=1
    if lst[i]=='':
        break
lst.remove('')
print(lst)
# Very important program. Solution idea by mom