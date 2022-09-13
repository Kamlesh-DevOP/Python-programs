import calendar 
y=int(input("enter the year YYYY : ")) 
m=int(input("enter the month MM : ")) 
a=calendar.month(y,m) 
s=a.index("Mo")
print(s)
a=(a[s:]) 
sun=21 
f=0 
for mon in range(0,sun,3): 
    temp=[] 
    for j in range(mon,len(a),sun): 
        mon=j
        val=(a[mon:mon+2]) 
        temp.append(val)  
    if "Fr" in temp and "13" in temp: 
        print("There is a friday with date 13th in. "+str(m)+" month of the year "+str(y)) 
        print(True) 
        f=1 
        break 
if f==0: 
    print(False) 
    print("There is no friday with date 13th in "+str(m)+" month of the year "+str(y))