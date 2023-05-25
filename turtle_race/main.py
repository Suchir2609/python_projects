import turtle
from turtle import Turtle,Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput(title="make your bet",prompt="which turtle will win the race? Enter a colour: ")

colors=["red",'blue','purple','orange','yellow','green',]
y_positions = [-100,-60,-20,20,60,100]
turtles=[]

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    turtles.append(new_turtle)

if user_input:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color==user_input:
                print(f"you've won! the {winning_color} turtle is the winner")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner")
        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()

