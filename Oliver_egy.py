print('8=="",==D')

import turtle

# Set up the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

# Draw the head of the dog
t.fillcolor("#8B4513")
t.begin_fill()
for i in range(36):
    t.forward(10)
    t.right(10)
for i in range(18):
    t.forward(5)
    t.right(10)
t.end_fill()

# Draw the ears
t.penup()
t.goto(-50, 50)
t.pendown()
t.fillcolor("#8B4513")
t.begin_fill()
for i in range(4):
    t.forward(40)
    t.right(90)
t.end_fill()

t.penup()
t.goto(50, 50)
t.pendown()
t.fillcolor("#8B4513")
t.begin_fill()
for i in range(4):
    t.forward(40)
    t.right(90)
t.end_fill()

# Draw the eyes
t.penup()
t.goto(-20, 30)
t.pendown()
t.fillcolor("#FFFFFF")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(20, 30)
t.pendown()
t.fillcolor("#FFFFFF")
t.begin_fill()
t.circle(10)
t.end_fill()

# Draw the nose
t.penup()
t.goto(0, 0)
t.pendown()
t.fillcolor("#000000")
t.begin_fill()
t.circle(5)
t.end_fill()

# Hide the turtle and exit on click
t.hideturtle()
screen.exitonclick()