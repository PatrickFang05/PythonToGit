import turtle
import random

turtle.screensize(2000, 2000)

t = turtle.Turtle()
t.shape('triangle')
t.color('green')
t.speed(2)

a = turtle.Turtle()
a.shape('triangle')
a.color('red')
a.speed(2)

b = turtle.Turtle()
b.shape('triangle')
b.color('blue')
b.speed(2)

c = turtle.Turtle()
c.shape('triangle')
c.color('purple')
c.speed(2)

t.penup()
t.goto(-200, 100)
t.pendown()
t.write(t.position())

a.penup()
a.goto(-200, 50)
a.pendown()
a.write(a.position())

b.penup()
b.goto(-200, 0)
b.pendown()
b.write(b.position())

c.penup()
c.goto(-200, -50)
c.pendown()
c.write(c.position())
foundWinner = False
for i in range(100):
    stepst = random.randint(1, 5)
    stepsa = random.randint(1, 5)
    stepsb = random.randint(1, 5)
    stepsc = random.randint(1, 5)
    t.forward(stepst)
    a.forward(stepsa)
    b.forward(stepsb)
    c.forward(stepsc)
    if t.xcor() >= 100:
        winner = t
        foundWinner = True
    elif foundWinner is False and a.xcor() >= 100:
        winner = a
        foundWinner = True
    elif foundWinner is False and b.xcor() >= 100:
        winner = b
        foundWinner = True
