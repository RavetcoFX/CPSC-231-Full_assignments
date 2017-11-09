#Assignment 3 - A game of nuts - Kieran Wood

#I have split the code up into sections to make it easier to jump between sections to mark;
#Section 1: All the general game functions that every case uses
#Section 2: All the Player vs Player specific functions
#Section 3: All the Player vs Untrained AI and Player vs Trained AI, aswell as the training functions

import random #The Library that will allow the random number generation needed in the Probability_Selection Function

#Section 1: General Functions used by every game Type
def How_Many_Nuts():
    """The function for asking and setting up the Amount of Nuts the Game will begin from: Takes no Arguments"""
    Amount_of_Nuts = int(input('How Many Nuts Are On the Table? (10-100): '))
    while ((Amount_of_Nuts > 100) or (Amount_of_Nuts < 10)):
        Amount_of_Nuts = int(input('Invalid Input; \nHow Many Nuts Are On the Table? (10-100): '))
    print(" \nAmount of Nuts Selected:%d \nThe game will begin from %d Nuts" %(Amount_of_Nuts, Amount_of_Nuts))
    return Amount_of_Nuts

def Player_Number(Amount_of_Nuts):
    """The Function that asks and determines the game type (player vs player, player vs AI) and initiates the game with the amount of nuts: Takes the amount of nuts as an argument"""
    Players = eval(input("\nOptions: \nPlay against a friend (1) \nPlay against an untrained computer (2) \nPlay against a trained AI (3) \nWhich Option do you take (1-3)?:"))
    Been_Selected = False #Value for if there has been a Valid input for the Players Variable
    while Been_Selected ==False:
        if Players == 1:
            print("\nPlayer vs Player Selected\n")
            Player_vs_Player(Amount_of_Nuts)
            Been_Selected = True
            break
        if Players ==2:
            print("\nPlayer vs Untrained AI Selected")
            Been_Selected = True
            break
        if Players ==3:
            print("\nPlayer vs Trained Ai Selected")
            print("\nTraining...")
            Been_Selected = True
            break
        else:
            Players = eval(input("\nInvalid Input \nOptions: \nPlay against a friend (1) \nPlay against an untrained computer (2) \nPlay against a trained AI (3) \nWhich Option do you take (1-3)?:"))

def Win_Condition(Amount_of_Nuts, Players, Turn_Number):
    """This is the function that determines whether or not the game has been won: Takes the amount of nuts, and Players Values as arguments"""
    Player_One_Win = False #will be used upon game end to determine which player won and print the corresponding name
    Player_Two_Win = False #will be used upon game end to determine which player won and print the corresponding name
    #print(Amount_of_Nuts)
    if Amount_of_Nuts <= 0: #if the last nut has been taken then the game should be over and thus Win is True
        Win = True
    else: #if the last nut has not been taken the game is still going and win is False
        Win = False
    
    if Win == True: #If the game is over, this will determine which player won and print the corresponding message
        print(Turn_Number%2)
        if (Turn_Number %2 == 0):
            Player_One_Win = True
        if (Turn_Number % 2 !=0):
            Player_Two_Win = True
        if (Player_One_Win == True): #if Player one print congratulations player one, since there is always a human player this does not need anymore specificity
            print("Congratulations Player One Won")
        if ((Player_Two_Win == True) and (Players == 1)): #if Player one won and it is a Player vs Player Game
            print("Congratulations Player Two Won")
        if ((Player_Two_Win == True) and (Players != 1)): #if The AI Won in any Player vs AI Game
            print("Congratulations the AI Won")
            
    return Win


def Main():
    print("Welcome to A game of Nuts!\n")
    Player_Number(How_Many_Nuts())





#Section 2: all functions specific to Player vs Player

def Player_Turn(Amount_of_Nuts, Win, Turn_Number):
    """This is the Function that defines what should happen during a players Turn: It takes the current Amount of Nuts and whether or not the game has been won as arguments"""
    if Win ==False:
        if ((Turn_Number%2) == 0):
            Player = "Two"
        else:
            Player = "One"
        print("\nPlayer %s Turn:" %(Player))
        print("\n%d Nuts Remaining\n" %(Amount_of_Nuts))
        Turn = eval(input("How Many Nuts Do you Take? (1-3):"))
        while ((Turn > 3) or (Turn < 1)):
            Turn = eval(input("\nInvalid input: \nHow Many Nuts Do you Take? (1-3):"))
        Amount_of_Nuts = (Amount_of_Nuts - Turn)
        if Amount_of_Nuts != 0: # No reason to print if Game is over here
            print("The Amount of Nuts Remaining is %d" %(Amount_of_Nuts))
    return Amount_of_Nuts


def Player_vs_Player(Amount_of_Nuts):
    """This is the function that defines what should happen if the Player vs Player mode is selected: It takes the initial Amount of nuts as  an argument"""
    Players = 1
    Turn_Number = 1 #is used to Let you Know what Turn number the Game is on for each Players turn + is used by Win_Condition to determine who won
    Win = Win_Condition(Amount_of_Nuts,Players, Turn_Number)#Initially sets up the Win Variable
    while Win == False:
            #Player Ones Turn
            Win = Win_Condition(Amount_of_Nuts,Players, Turn_Number)
            Amount_of_Nuts = Player_Turn(Amount_of_Nuts,Win, Turn_Number)
            Turn_Number += 1
            #Player two's Turn
            Win = Win_Condition(Amount_of_Nuts,Players, Turn_Number) #Updates Win Variable before Player One's Turn
            Amount_of_Nuts = Player_Turn(Amount_of_Nuts,Win, Turn_Number)
            Turn_Number += 1













Main()