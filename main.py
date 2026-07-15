from turtle import Turtle, Screen

import random
is_race_on = False
my_screen = Screen()
my_screen.setup(width= 600, height=500)
bet = 0

user_bet = my_screen.textinput(title = "Make your Bet!", prompt= "Which turtle will win the race? Enter a color: ", )
bet = my_screen.numinput(title = "Bet" , prompt ="How much are you staking: " , minval= 100)


colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "black", "Cyan", "violet", "indigo"]

all_turtles = []

y_postion = [-230, -200, -170, -140, -110, -80, -50, -20, 10,40,70]
for turtle_index in range (0,11):
    my_turtle = Turtle("turtle")
    my_turtle.color(colors[turtle_index])
    my_turtle.penup()
    my_turtle.goto(x = -280, y =y_postion[turtle_index])
    all_turtles.append(my_turtle)


if bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                bet += 100
                print(f"You've won! The {winning_color} turtle is the winner! Your balance is ${bet}")
            else:

                bet -= 100
                print(f"You lost, The {winning_color} turtle is the winner!, Your balance is ${bet}")


        random_distance = random.randint(0,10)
        turtle.forward((random_distance))






my_screen.exitonclick()