car_type=input('Enter the car type')
sp=int(input('Enter the cost of the car excluding discount'))
if car_type == 'suv':
    print('Total cost is ',sp-(10/100)*sp)
elif car_type == 'sedan':
    print('Total cost is ',sp-(20/100)*sp)
elif car_type=='maruthi':
    print('Total cost is ',sp-(15/100)*sp)
else:
    print('invalid car type')
