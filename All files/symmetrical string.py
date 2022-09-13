#ramram coco are examples
st=input('Enter a string: ')
if len(st)%2==1:
    print('Not symmetrical')
else:
    firsthalf=st[:int(len(st)/2)]
    secondhalf=st[int(len(st)/2):]
    if firsthalf==secondhalf:
        print('It is a symmetrical name')
