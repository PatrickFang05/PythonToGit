import turtle

dad = turtle.Turtle()
dad.color('blue')
dad.fillcolor('orange')
dad.shape('circle')
turtle.speed(5)
for i in range(3):
    turtle.forward(60)
    turtle.left(120)
turtle.penup()
turtle.forward(-300)
turtle.pendown()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.pendown()
for i in range(5):
    turtle.forward(70)
    turtle.left(72)
turtle.penup()
turtle.right(270)
turtle.forward(400)
turtle.pendown()
for i in range(6):
    turtle.right(60)
    turtle.forward(60)
