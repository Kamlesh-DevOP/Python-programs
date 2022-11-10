import turtle
sides=int(input('Enter number of sides: '))
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('brown')
t.pencolor('blue')
t.penup()
t.width(10)
t.goto(-200,250)
t.pendown()
a=5
for i in range(sides):
    t.forward(200)
    t.speed(a)
    a+=2*i
    t.right(360/sides)
