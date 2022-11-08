#https://leetcode.com/problems/richest-customer-wealth/description/
l=[]
accounts=eval((input('Enter list: ')))
for i in accounts:
    count=0
    for j in i:
        count+=j
    l.append(count)
print((max(l)))