import random
import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('brown')
t.pencolor('blue')
t.penup()
t.goto(-400,290)
t.write('Welcome to the hangman game:',True,'left',('Comic Sans MS',40))
word='thanks'
x=input('Enter letter: ')
if x not in word:
    t.penup()
    t.goto(200,-200)
    t.pendown()
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.color('black')
    t.fillcolor()
    t.circle(20)
    t.end_fill()
    t.forward(100)








        
