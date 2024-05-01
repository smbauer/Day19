from turtle import Turtle, Screen


def move_forwards():
    """move turtle instance forwards by 10 paces"""
    t.forward(10)


def move_backwards():
    """move turtle instance backwards by 10 paces"""
    t.backward(10)


def turn_left():
    """turn turtle instance left by 10 degrees"""
    t.left(10)


def turn_right():
    """turn turtle instance right by 10 degrees"""
    t.right(10)


def reset_screen():
    """clear the screen and return turtle instance to the origin"""
    screen.reset()


# initialize turtle and screen objects
t = Turtle()
screen = Screen()

# bind keys to functions
# W - Forwards
screen.onkey(fun=move_forwards, key='w')
# S - Backwards
screen.onkey(fun=move_backwards, key='s')
# A - Counter-clockwise
screen.onkey(fun=turn_left, key='a')
# D - Clockwise
screen.onkey(fun=turn_right, key='d')
# C - Clear drawing and return turtle to origin (0,0)
screen.onkey(fun=reset_screen, key='c')

screen.listen()
screen.exitonclick()
