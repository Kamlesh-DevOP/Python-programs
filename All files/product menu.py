'''13WAP to input 'n' company names as keys; the values should be a nested
dictionary whose key will be a product name & value will be the price
eg : D= {'SONY': {'TV': 56000, 'MOBILE' : 32000, 'LAPTOP': 45000}, 'HP': {'Printer': 12000, 'PC': 25000}} & do the
following:
1. Print products company wise
2. Print only company name
3. Print company, product, price in tabular form
4. search for a company & if found print its details'''
import json
d={}
n=int(input('Enter n: '))
for i in range(n):
    d1={}
    company=input('Enter company name: ')
    no_of_prods=int(input('Enter number of products: '))
    for j in range(no_of_prods):
        product=input('Enter product name: ')
        price=int(input('Enter price: '))
        d1[product]=price
    d[company]=d1

print('''
1. Print products company wise
2. Print only company name
3. Print company, product, price in tabular form
4. search for a company & if found print its details''')

while True:
    choice=int(input('Enter 1 2 3 or 4: '))
    if choice ==1:
        for i in d:
            print(i,':')
            for j in d[i]:
                print('\t',j)
    elif choice==2:
        for i in d:
            print(i)
    elif choice==3:
        print('Company\tProduct\tPrice')
        for i in d:
            for j in d[i]:
                print(i,'\t',j,'\t',d[i][j])
    elif choice==4:
        comp=input('Enter company to search: ')
        for i in d:
            if i.lower()==comp.lower():
                print(json.dumps(d[i],indent=2))
