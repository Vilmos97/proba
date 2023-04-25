print('8=="",==D')

import turtle

# Set up the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

# Draw the head of Peter Griffin
t.fillcolor("#F2C640")
t.begin_fill()
t.circle(60)
t.end_fill()

# Draw the eyes
t.penup()
t.goto(-30, 70)
t.pendown()
t.fillcolor("#FFFFFF")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(30, 70)
t.pendown()
t.fillcolor("#FFFFFF")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-25, 75)
t.pendown()
t.fillcolor("#000000")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(25, 75)
t.pendown()
t.fillcolor("#000000")
t.begin_fill()
t.circle(10)
t.end_fill()

# Draw the mouth
t.penup()
t.goto(-30, 50)
t.pendown()
t.right(45)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(135)

# Draw the body
t.penup()
t.goto(0, -80)
t.pendown()
t.fillcolor("#F2C640")
t.begin_fill()
for i in range(2):
    t.forward(80)
    t.right(90)
    t.forward(150)
    t.right(90)
t.end_fill()

# Draw the legs
t.penup()
t.goto(-30, -80)
t.pendown()
t.fillcolor("#FFFFFF")
t.begin_fill()
for i in range(2):
    t.forward(40)
    t.right(90)
    t.forward(80)
    t.right(90)
t.end_fill()

t.penup()
t.goto(30, -80)
t.pendown()
t.fillcolor("#FFFFFF")
t.begin_fill()
for i in range(2):
    t.forward(40)
    t.right(90)
    t.forward(80)
    t.right(90)
t.end_fill()

# Hide the turtle and exit on click
t.hideturtle()
screen.exitonclick()