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
def init_alex():
    """defining the turtle in here hopefully will make it so Take_turns can see alex and in turn user_move cant see the turtle"""
    alex = turtle.Turtle()
    return alex
def init_alice():
    """defining the turtle in here hopefully will make it so Take_turns can see alice and in turn alice_move cant see the turtle"""
    alice = turtle.Turtle()
    return alice
def user_move(alex):
    """Function for defining what should happen during the players move"""
    op = 0
    while op == 0:
        #old useless code unless you can prompt by string inputs, just using for debugging
        dir = input('prompt:')
        if (('w') or ('W')) in dir:
            alex.fd(30)
            op = 1
            print('forward')
        if (('s') or ('S')) in dir:
            alex.fd(-30)
            op = 1
            print('backward')
        if (('a') or ('A')) in dir:
            alex.lt(45)
            op = 1
            print('left')
        if (('d') or ('D')) in dir:
            alex.rt(45)
            op = 1
            print('right')
        if op == 0:
            op=0
            print('invalid input')

def win_condition():
    """this will be the function that decides if the game is over"""
    return False
    #need an if statement for alice and alex within 30 pixels

def Alice_move(alice):
    """This will be the function that executes alices move after the player"""
    numb = (random.uniform(1,6))//1
    print(numb)
    if numb == 1:
        alice.lt(45)
    if numb==2:
        alice.rt(45)
    else:
        alice.fd(30)
    pass

def Take_Turns(alex,alice):
    """The function that calls each players turns to take place while the game hasn't been won"""
    while win_condition()==False:
        user_move(alex)
        Alice_move(alice)


def main():
    qq = turtle.Screen() #makes it so I don't have to type out turtle.screen()
    Take_Turns(init_alex(), init_alice())
    qq.mainloop()


main()
