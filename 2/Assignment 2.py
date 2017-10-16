import tkinter as tk
import turtle
import random

#need it to be 2/3rds of the time moving forward
#random.randint(range)
def forward():
    """makes alex move forward 30 pixels"""
    alex.fd(30)
def turn_left():
    """makes alex turn 45 degrees left"""
    alex.lt(45)
def turn_right():
    """makes alex turn 45 degrees right"""
    alex.rt(45)
def Backward():
    """makes alex move backward 30 pixels"""
    alex.fd(-30)

def user_move():
    """Function for defining what should happen during the players move"""
    op = 0
    while op < 1:
        #old useless code unless you can prompt by string inputs, just using for debugging
        dir = input('prompt')
        if dir == 'w'or 'W':
            alex.fd(5)
            op = 1
        if dir == 's' or 'S':
            alex.fd(-5)
            op = 1
        if dir == 'a' or 'A':
            alex.lt(45)
            op = 1
        if dir == 'd' or 'D':
            alex.rt(45)
            op = 1
        
        #setting up the listner
        #turtle.Screen().onkey(forward,"w")
        #turtle.Screen().onkey(turn_left,"a")
        #turtle.Screen().onkey(turn_right,"d")
        #turtle.Screen().onkey(Backward,"s")
        #turtle.Screen().listen()
    else:
            print('invalid input')
            op=0

def win_condition():
    """this will be the function that decides if the game is over"""
    return False
    #need an if statement for alice and alex within 30 pixels

def Alice_move():
    """This will be the function that executes alices move after the player"""
    pass

def Take_Turns():
    """The function that calls each players turns to take place while the game hasn't been won"""
    while win_condition()==False:
        user_move()
        Alice_move()

#random number generation
random.uniform(0,1)
print(random.uniform(1,2))

def main():
    qq = turtle.Screen() #makes it so I don't have to type out turtle.screen()
    alex = turtle.Turtle() #defining the turtle in here makes it so Take_turns can't see and in turn user_move cant see the turtle
    Take_Turns()
    qq.mainloop()


main()
