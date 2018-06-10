import turtle
import random

numTurtles = int(turtle.numinput('race', 'How many turtles?'))
colors = ['red', 'blue', 'green', 'purple', 'black', 'magenta', 'cyan', 'brown']

turtle.screensize(2000, 2000)

turtles = []
# Create each turtle object and push them to the turtles list
for i in range(numTurtles):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(colors[i])
    t.speed(1)
    turtles.append(t)

# Position each turtle at their starting coordinates
for i in range(numTurtles):
    t = turtles[i]
    t.penup()
    t.goto(-250, 100 - 30 * i)
    t.pendown()

# Set up empty winner variable
winner = ''

# Let all the turtles move 100 steps at a random pixel in each step
for j in range(50):
    for i in range(numTurtles):
        steps = random.randint(1, 5)
        turtles[i].forward(steps)

# Print all the turtles' final position
for i in range(numTurtles):
    turtles[i].write(turtles[i].position())

turtle.done()
