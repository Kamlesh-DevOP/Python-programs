import csv
with open('D:/python/GST.csv','w+',newline='') as f:
    w=csv.writer(f)
    w.writerow(['Category','GST Percentage'])
    w.writerow(['Automobiles','25'])
    w.writerow(['Stationary','12'])
    w.writerow(['Chocolates','10'])
    w.writerow(['Dairy','3'])
with open(r'ITEMS.csv','w+',newline='') as f:
    w=csv.writer(f)
    w.writerow(['ItemID','Name','Category','Unitprice','Finalprice'])
    n=int(input('Enter n: '))
    for i in range(n):
        ItemID=int(input('Enter item ID: '))
        Name=input('Enter name: ').capitalize()
        Category=input('Enter category: ').capitalize()
        Unitprice=int(input('Enter unit price: '))
        with open(r'GST.csv') as f1:
            r1=csv.reader(f1)
            for i in r1:
                if Category in i:
                    gst=int(i[1])
        Finalprice=Unitprice+(gst/100)*Unitprice
        w.writerow([ItemID,Name,Category,Unitprice,Finalprice])
    print('Changes made in ITEMS.csv')
with open(r'ITEMS.csv') as f:
    r=csv.reader(f)    
    for record in r:
        print(record)

'''   
Enter n: 4   
Enter item ID: 1
Enter name: milk
Enter category: dairy
Enter unit price: 25
Enter item ID: 2
Enter name: pen
Enter category: stationary
Enter unit price: 40
Enter item ID: 3
Enter name: car
Enter category: automobiles
Enter unit price: 500000
Enter item ID: 4
Enter name: lindor
Enter category: chocolates
Enter unit price: 1100
Changes made in ITEMS.csv
['ItemID', 'Name', 'Category', 'Unitprice', 'Finalprice']
['1', 'Milk', 'Dairy', '25', '25.75']
['2', 'Pen', 'Stationary', '40', '44.8']
['3', 'Car', 'Automobiles', '500000', '625000.0']        
['4', 'Lindor', 'Chocolates', '1100', '1210.0']'''