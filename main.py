import turtle as t

tim = t.Turtle()
screen = t.Screen()

def forward(): #to move the turtle forward
    tim.forward(10)
def backward(): #to move the turtle backward
    tim.back(10)
def left(): # to turn the turtle left
    tim.left(10)
def right(): # to turn the turtle right
    tim.right(10)
def clear(): # to clear the screen
    tim.clear()
def recenter(): # to make the turtle return to starting position
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen() # it listens to the key presses

#moves forward on pressing w
screen.onkey(fun=forward,key="w") #No () at the end of the function so that it doesn't execute on it's own and waits for "Up" being pressed
#turns left on pressing a
screen.onkey(fun=left,key="a")
#turns right on pressing d
screen.onkey(fun=right,key="d")
#moves backward on pressing s
screen.onkey(fun=backward,key="s")
#clears the screen on pressing c
screen.onkey(fun=clear,key="c")
#recenters the turtle on pressing r
screen.onkey(fun=recenter,key="r")

#waits for a click to exit the window
screen.exitonclick()