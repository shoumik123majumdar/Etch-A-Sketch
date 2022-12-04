from turtle import Turtle, Screen

bobe = Turtle()
screen = Screen()



def forwards():
    bobe.forward(10)
def backwards():
    bobe.back(10)
def turnLeft():
    newheading = bobe.heading() + 10
    bobe.setheading(newheading)
def turnRight():
    newerheading = bobe.heading() - 10
    bobe.setheading(newerheading)
def clear():
    bobe.clear()
    bobe.penup()
    bobe.home()
    bobe.pendown()

screen.listen()
screen.onkey(forwards,"w")
screen.onkey(backwards,"s")
screen.onkey(turnLeft, "a")
screen.onkey(turnRight,"d")
screen.onkey(clear, "c")





screen.exitonclick()

