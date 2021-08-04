import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

t.color("blue")

t.begin_fill()
t.fillcolor("blue")


t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)

t.end_fill()
t.hideturtle()