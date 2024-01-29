import csv
with open('csvfile.csv','r',newline='') as f:
    r=csv.reader(f)
    l=[]
    for i in r:
        l.append(i)
    print(l)

