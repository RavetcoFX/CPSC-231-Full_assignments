import turtle
import random


def init_alex():
    """defining the turtle in here hopefully will make it so Take_turns can see alex and in turn user_move cant see the turtle"""
    alex = turtle.Turtle()
    alex.shape("turtle")
    alex.pencolor('Blue')
    alex.fillcolor("Blue")
    return alex
def init_alice():
    """defining the turtle in here hopefully will make it so Take_turns can see alice and in turn alice_move cant see the turtle"""
    alice = turtle.Turtle()
    alice.shape("turtle")
    alice.pencolor("Red")
    alice.fillcolor("Red")
    return alice
def use_turtles(alex,alice):
    """A function that allows you to call each turtle without recreating the turtle each time"""
    alex = alex
    alice = alice
    return [alex,alice]
def user_move(alex, alice):
    """Function for defining what should happen during the players (alex's) move"""
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
        if ('cheat') in dir:
            Alice_move(alice, True, alex.pos())
            op = 2
            print('cheater')
        if op == 0:
            op=0
            print('invalid input')
        if op == 2:
            pass
def startpoint(turtles):
    """Function that carries out the movement of each turtle to a random location in the canvas at the start of each game"""
    alex = turtles[0]
    alice = turtles[1]
    alex.up()
    alex.setpos((random.randint(0,500)),(random.randint(0,500)))
    alex.down()
    alice.up()
    alice.setpos((random.randint(0,500)),(random.randint(0,500)))
    alice.down()
    return turtles

def Alice_move(alice, cheat, other_pos):
    """This will be the function that executes alices move after the player"""
    numb = (random.uniform(1,6))//1
    if cheat:
        alice.setposition((other_pos[0])//1,(other_pos[1])//1)
        pass
    if numb == 1:
        alice.lt(45)
    if numb==2:
        alice.rt(45)
    else:
        alice.fd(30)
    pass

def Take_Turns(turtles):
    """The function that calls each players turns to take place while the game hasn't been won"""
    win = False
    while not win:
        alex= turtles[0]
        alice= turtles[1]
        user_move(alex, alice)
        Alice_move(alice, False, None)
        if ((alex.distance(alice,alice)) // 1) < 100:
            win = True
            print("you win") #Maybe print to the window later
            turtle.clearscreen()
            main()
            


def main():
    qq = turtle.Screen() #makes it so I don't have to type out turtle.screen()
    #startpoint(init_alex(), init_alice())
    Take_Turns(startpoint(use_turtles(init_alex(), init_alice())))
    qq.mainloop()


main()
