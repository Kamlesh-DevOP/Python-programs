ang=int(input('Enter an angle: '))
ang=ang%360
if ang>=0 and ang<=90:
    print('I')
elif ang>90 and ang<=180:
    print('II')
elif ang>180 and ang<=270:
    print('III')
else:
    print('IIII')