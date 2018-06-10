import turtle

star = turtle.Turtle()
star.color('red')
star.fillcolor('blue')
star.speed(4)
for i in range(5):
    star.right(136)
    star.forward(50)
    star.left(64)
    star.forward(50)
star.penup()
star.right(90)
star.forward(200)
star.pendown()
for i in range(5):
    star.forward(70)
    star.right(144)
