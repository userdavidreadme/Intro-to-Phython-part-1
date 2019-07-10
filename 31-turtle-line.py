import turtle

window = turtle.Screen()

lines= turtle.Turtle()

# pen settings
lines.pencolor("Red")
lines.pensize(12)
lines.shape("turtle")

lines.forward(50)
lines.left(90)
lines.forward(200)

window.exitonclick()
