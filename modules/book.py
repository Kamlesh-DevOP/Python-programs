import csv
with open('book.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['rno','name'])
    w.writeheader()
    w.writerow({'rno':'1','name':'kamlesh'})
    w.writerow({'rno':'2','name':'rathish'})
    w.writerow({'rno':'3','name':'arjun'})
with open('book.csv','r') as f:
    l=csv.DictReader(f)
    for d in l:
        for key in d:
            print(d[key],end=' ')
        print()
    #or 
    r=csv.DictReader(f)
    for k in r:
        print(k['rno'],k['name'])

    