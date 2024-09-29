from turtle import *
from random import randint

width = 200

t1 = Turtle()
t1.color("purple")
t1.shape("turtle")
t1.penup()
t1.goto(-width, 25)

t2 = Turtle()
t2.color("orange")
t2.shape("turtle")
t2.penup()
t2.goto(-width, 50)

def win(t):
    t.goto(0, 100)
    t.pendown()
    for i in range(30):
        t.forward(2 * i)
        t.left(90)

    t.write("I WIN!", False, font=("Consolas", 24 ))


while t1.xcor() < width and t2.xcor() < width:
    t1.forward(randint(5, 10))
    t2.forward(randint(5, 10))

if t1.xcor() < t2.xcor():
    win(t2)
else:
    win(t1)

exitonclick()