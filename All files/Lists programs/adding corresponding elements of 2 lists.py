l1=eval(input('Enter a list: '))
l2=eval(input('Enter a list: '))
sum_list=[]
for i in range(len(l1)):
    sum_list.append(l1[i]+l2[i])
print(sum_list)