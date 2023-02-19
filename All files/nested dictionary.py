'''13. Write a Python code to create a dictionary of ‘n’ items (Name of item will be the key and value will be a
nested dictionary with stock, price ) by reading values from user. Read another such nested dictionary with
freshly arrived ‘m’ items(Name, stock, price). Update the 1st dictionary using the 2nd dictionary – i.e if item
name of 2nd dictionary exists in the 1st dictionary, increase the stock of that item in the 1st dictionary. If item
name does not exist, include the detail as a new item in the 1st dictionary. Display the updated dictionary.
(eg) if D1 has: { “Soap”: { “Stock”:50, “Price”: 25 }, “Tea” : {“Stock”: 20,

“Price”: 35.00} }

if D2 has: { “Soap” :{“Stock”:100, “Price”: 25}, “Pen”:{“Stock”:50, “Price”:

17.50} }

D1 should become: {“Soap”: {“Stock”:150, “Price”:25}, “Tea” : {“Stock”: 20,
“Price”: 35.00}, “Pen”:{“Stock”:50, “Price”: 17.50} } '''

n=int(input('Enter number of entries: '))
d1={}
for i in range(n):
    prod1=input('Enter product name: ')
    stock1=int(input('Enter number of stock: '))
    price1=int(input('Enter price: '))
    d1[prod1]={'stock':stock1,'price':price1}
print(d1)
d2={}
for i in range(n):
    prod2=input('Enter product name: ')
    stock2=int(input('Enter number of stock: '))
    price2=int(input('Enter price: '))
    d2[prod2]={'stock':stock2,'price':price2}
print(d2)

for key2 in d2:
    if key2 not in d1:
        d1[key2]=d2[key2]
    else:
        d1[key2]['stock']+=d2[key2]['stock']

print(d1)
