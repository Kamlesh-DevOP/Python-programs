cm=int(input('Enter lenth in centimeter'))
inch=cm/2.54
#inch is just converting cm to inch
feet=inch//12
inches=inch%12
#inches is to convert inch to feet and the remaining inches
print(round(inches,2),'inches and', feet,'feet')
print(' '*50, '(or)')
print(round(inch,2), 'inch',)

