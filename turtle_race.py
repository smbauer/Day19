from turtle import Turtle, Screen
from random import randint

# set up the screen
screen = Screen()
screen.setup(width=500, height=400, startx=None, starty=None)

# turtle instance parameters
num_turtles = 6
colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
y_starts = [125, 75, 25, -25, -75, -125]

# initialize turtles
for i in range(num_turtles):
    t = Turtle(shape='turtle')
    t.color(colors[i])
    t.penup()
    t.setpos(x=-230, y=y_starts[i])

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a colour: ")

race_on = True

while race_on:
    for turtle in screen.turtles():
        # move turtles forward by a random amount each step
        turtle.forward(randint(1, 20))
        if turtle.xcor() >= 230:
            # end game when any turtle reaches the end of the screen
            race_on = False
            winner = turtle.pencolor()

print(f"Winner is {winner}!")

if winner == user_bet:
    print("You won!")
else:
    print("You lost :(")

screen.exitonclick()
