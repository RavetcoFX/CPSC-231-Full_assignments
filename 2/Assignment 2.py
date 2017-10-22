import turtle #The library that will handle all the players, window and the majority of the games functionality
import random #Library used to generate random numbers for the spawn positions of the players + deciding Alice's moves
import time # Used to delay the end of the game so you can read the "You Win" 


def init_jeff():
    """The function that initializes the turtle(jeff) that will handle writing text for the distance between alice and alice, as well as the turn/step number"""
    jeff = turtle.Turtle()
    Top_left_corner = (-240,220) # the coordinate value for ~ the top left corner
    jeff.hideturtle()
    jeff.up()
    jeff.setpos(Top_left_corner) #moving to a value close to the top left of the screen so as it does not get in the way while playing
    return jeff
    
def init_alex():
    """defining the turtle in here hopefully will make it so Take_turns can see alex and in turn user_move cant see the turtle"""
    alex = turtle.Turtle()
    #the values for shape, pen color, and fill color are based on the assignment requirements
    alex.shape("turtle")
    alex.pencolor('Blue')
    alex.fillcolor("Blue")
    return alex

def init_alice():
    """defining the turtle in here hopefully will make it so Take_turns can see alice and in turn alice_move cant see the turtle"""
    alice = turtle.Turtle()
    #the values for shape, pen color, and fill color are based on the assignment requirements
    alice.shape("turtle")
    alice.pencolor("Red")
    alice.fillcolor("Red")
    return alice

def use_turtles(alex,alice):
    """A function that allows you to call each turtle without recreating the turtle each time; needs both alex and alice as arguments"""
    alex = alex
    alice = alice
    return [alex,alice]
    
def startpoint(turtles, window_height_width):
    """Function that carries out the movement of each turtle to a random location in the canvas at the start of each game; needs both turtles as a list + the max value of the window for arguments"""
    alex = turtles[0] #strips alex from the list of [alex, alice] in use_turtles()
    alice = turtles[1] #strips alice from the list of [alex, alice] in use_turtles()
    max_limit = ((window_height_width//2) - 10) #Uses the windows maximum height and width value -10 so that the turtles cannot spawn outside the screen
    
    alex.up()#so that when alex gets moved a line isnt drawn from (0,0) to the location
    alex.setpos((random.randint(0,max_limit)),(random.randint(0,max_limit))) #after spawning alex, move to a random location within the canvas; this will be the starting position for alex
    alex.down()
    
    alice.up() #so that when alice gets moved a line isnt drawn from (0,0) to the location
    alice.setpos((random.randint(0,max_limit)),(random.randint(0,max_limit)))#after spawning alice, move to a random location within the canvas; this will be the starting position for alice
    alice.down()
    return turtles


def user_move(alex, alice):
    """Function for defining what should happen during the players (alex's) move; needs both alex and alice as an input argument"""
    Alex_Forward_by = 30 # The amount of pixels alex should move forward by
    Alex_Turn_by = 45 #The angle, in degrees that Alex should turn in a direction by
    is_invalid_input = 0 #arbitrary variable to handle invalid inputs
    while is_invalid_input == 0:
        direction = input('Move Alex:') #Takes a string input that then gets checked through all the if statements and performs an action
        if (('w') or ('W')) is direction:
            alex.fd(Alex_Forward_by)
            is_invalid_input = 1
            
        if (('a') or ('A')) is direction:
            alex.lt(Alex_Turn_by)
            is_invalid_input = 1
            
        if (('d') or ('D')) is direction:
            alex.rt(Alex_Turn_by)
            is_invalid_input = 1
            
        #Code for automatically winning the round; used to test win condition
       # if ('cheat') in direction:
        #    alex.setpos(alice.pos())
         #   print('cheater')
          #  is_invalid_input = 1
        if is_invalid_input == 0:
            is_invalid_input=0
            print('invalid input please input one of these values \nw= forward \na= left turn \nd = right turn')

def Fix_Offscreen(name):
    """Function for handling (in a way similar to pacman) if the turtles move out of the canvas (off screen); the only argument passed is the name of the turtle"""
    Negative_Max = -250 #The lowest possible x or y value that is within the canvas
    Negative_Max_New = 240 #The coordinate to relocate the turtle to if they go past Negatice_Max value in the x or y
    Positive_Max = 250 #The Highest possible x or y value that is within the canvas
    Positive_Max_new = -240 ##The coordinate to relocate the turtle to if they go past the Positive_Max value in the x or y
    if name.xcor() <= Negative_Max:
        name.up()
        name.ht()
        name.setx(Negative_Max_New)
        name.down()
        name.st()
    if name.xcor() >= Positive_Max:
        name.up()
        name.ht()
        name.setx(Positive_Max_new)
        name.down()
        name.st()
    if name.ycor() >= Positive_Max:
        name.up()
        name.ht()
        name.sety(Positive_Max_new)
        name.down()
        name.st()
    if name.ycor() <= Negative_Max:
        name.up()
        name.ht()
        name.sety(Negative_Max_New)
        name.down()
        name.st()


def Alice_move(alice, alex):
    """This will be the function that executes alices move after the player"""
    Alice_Forward_by = 20 # The amount of pixels alice should move forward by
    Alice_Turn_by = 90 #The angle, in degrees that Alice should turn in a direction by
    numb = (random.uniform(1,6))//1 #Does the random number generation that determines Alice's turn
    if alex.pos() == alice.pos():
        pass
    if numb == 1:
        alice.lt(Alice_Turn_by)
    if numb==2:
        alice.rt(Alice_Turn_by)
    else:
        alice.fd(Alice_Forward_by)
    pass

def win_condition(alex, alice, jeff, each_turn_count):
    """Handles determining if the game is won or not; if the game is won it will restart the game, if not it will let each turtle take their turn"""
    win = False #Initially set win to False as long as alex and alice did not spawn within 30 pixels
    while not win: #While the game still hasn't been won each player takes their turn, and jeff presents the games information until the game is won
        each_turn_count += 1 #The value for which turn the game is on; used by jeff to present this information to the player
        jeff.write(('Step #%i - The distance between Alex and Alice is: %i' % (each_turn_count, ((alex.distance(alice,alice))) // 1)), False, align="left") #Jeff will write the turn/step# + the distance between the turtles each turn
        user_move(alex, alice) #Alex takes his turn
        Fix_Offscreen(alex) #checks to make sure Alex is not outside the boundary; if he is then fix it
        Alice_move(alice, alex) #Alice takes her turn
        Fix_Offscreen(alice)#checks to make sure Alice is not outside the boundary; if he is then fix it
        jeff.clear() #after each turn the text has to be cleares so that it does not overlap with the last turn
        if ((alex.distance(alice,alice)) // 1) < 30 and alex.isdown() and alice.isdown(): # if you win jeff writes you win, the title of the window changes and after 3 seconds the screen clears and the game restarts
            win = True
            jeff.clear()
            jeff.write("You Win")
            turtle.Screen().title("You Win - Game will restart shortly")
            time.sleep(3)
            turtle.clearscreen()
            main()

def Game_loop(turtles):
    """The function that brings in all the turtles after their setup stages, sets the turn count to 0, then calls the win_condition funciton"""
    alex= turtles[0]
    alice= turtles[1]
    jeff = init_jeff()
    each_turn_count = 0
    win_condition(alex, alice, jeff, each_turn_count)
    

def main():
    window_height_width = 500 #This is the maximum Height and Width of the window 
    turtle.Screen().setup(window_height_width,window_height_width) #uses the window_height_width value to create a square aspect ratio window (i.e. 500x500)
    turtle.Screen().title("Assignment 2 - Chasing Alice - Kieran Wood") #This sets the Turtle window to the right name
    Game_loop(startpoint(use_turtles(init_alex(), init_alice()), window_height_width)) #This calls all the functions in the right order to play the game; initializes the turtles and passes them as arguments to use_turtles, which is then brought into startpoint and then brought into the main game loop
    
    
main()
