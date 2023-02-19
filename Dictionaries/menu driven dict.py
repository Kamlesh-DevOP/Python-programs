'''WAP to create a dictionary ITEM to have as key the prod ID,#as value a nested dictionary with details of
productname, price & stock'''
print('''
1. Display all items
2. Increase the price of a given product ID by a given amount
3. Item name with the max price
4. Remove all items with stock less than 10''')

n=int(input('Enter number of entries: '))
d = {}
for i in range(n):
    id = int(input("Enter ID: "))
    name = input("Enter product name: ")
    price = int(input("Enter price: "))
    stock = int(input("Enter stock: "))
    d[id] = {"Name": name, "Price": price, "Stock": stock}
print(d)
choice=int(input('Enter choice: '))

while choice>0 and choice<5:

    if choice==1:
        print(d) #{1: {'soap': [100, 10]}, 2: {'pen': [5, 19]}}
    elif choice==2:
        pid = int(input("Enter product ID: "))
        amt = int(input("Enter increment: "))
        for i in d:
            if i==pid:
                d[i]["Price"] += amt
        print(d)
        print()

    elif choice==3:
        L=[]
        for i in d:
            L.append(d[i]["Price"])
        maxprice = max(L)
        for i in d:
            if d[i]["Price"] == maxprice:
                print("Item name with max price:",d[i]['Name'])
        print()

    elif choice==4:
        d2=d.copy()
        for i in d:
            if d[i]["Stock"] < 10:
                d2.pop(i)
        d=d2
        print(d)
        print()
    choice=int(input('Enter choice'))




    
