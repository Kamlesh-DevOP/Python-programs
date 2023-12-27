import csv
with open('testing.csv','r') as f:
    r=csv.reader(f)
    print(sorted(r))