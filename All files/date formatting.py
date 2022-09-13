date=int(input('Date: '))
month= int(input('Month: '))
year=int(input('Year: '))
if month==1:
    mon='January'
elif month==2:
    mon='February'
elif month==3:
    mon='March'
elif month==4:
    mon='April'
elif month==5:
    mon='May'
elif month==6:
    mon='June'
elif month==7:
    mon='July'
elif month==8:
    mon='August'
elif month==9:
    mon='September'
elif month==10:
    mon='October'
elif month==11:
    mon='November'
elif month==12:
    mon='December'
else: mon='Invalid month'
print(date,mon,year)