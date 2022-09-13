q=int(input('What do you want to do? 1 for area of circle 2 for circumference 3 for exit '))
if q==1:
    radius=int(input('Enter radius of the circle: '))
    area=3.14*radius**2
    print('Area is',area)
elif q==2:
    radius=int(input('Enter radius of the circle: '))
    cir=2*3.14*radius
    print('Circumference is',cir)
elif q==3:
    quit()