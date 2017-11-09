#Assignment 3 - A game of nuts - Kieran Wood

#I have split the code up into sections to make it easier to jump between sections to mark;
#Section 1: All the general game functions that every case uses
#Section 2: All the Player vs Player specific functions
#Section 3: All the Player vs Untrained AI 
#Section 4: Player vs Trained AI, aswell as the training functions (Not Complete)

import random #The Library that will allow the random number generation needed in the Probability_Selection Function

#Section 1: Defining the functions that will be used for each case of the game; Player vs Player, Player vs Untrained AI, Player vs Trained AI
def How_Many_Nuts():
    """The function for asking and setting up the Amount of Nuts the Game will begin from: Takes no Arguments"""
    Amount_of_Nuts = int(input('How Many Nuts Are On the Table Initially? (10-100): '))
    while ((Amount_of_Nuts > 100) or (Amount_of_Nuts < 10)): # as long as the values are exceeding range(input is invalid; Too high, or too low)
        Amount_of_Nuts = int(input('Invalid Input; \nHow Many Nuts Are On the Table? (10-100): '))
    print(" \nAmount of Nuts Selected:%d \nThe game will begin from %d Nuts" %(Amount_of_Nuts, Amount_of_Nuts))
    return Amount_of_Nuts     
def Player_Number(Amount_of_Nuts):
    """The Function that asks and determines the game type (player vs player, player vs AI) and initiates the game with the amount of nuts: Takes the amount of nuts as an argument"""
    Players = eval(input("\nOptions: \nPlay against a friend (1) \nPlay against an untrained computer (2) \nPlay against a trained AI (3)(Not Working) \nWhich Option do you take (1-3)?:"))
    Been_Selected = False #Value for if there has been a Valid input for the Players Variable
    Win = Win_Condition(Amount_of_Nuts) # Because this is the outermost function being called in the Main function it needs to know if it should terminate
    while ((Been_Selected ==False) and (Win == False)):
        if Players == 1: # two player game
            print("\nYou have selected a two Player game")
            Been_Selected = True
            Player_vs_Player(Amount_of_Nuts,Players)
            break
        if Players ==2: # Selection corresponding to an untrained AI
            print("\nYou have selected to play against an untrianed AI")            
            Untrrained_AI(Amount_of_Nuts)
            Been_Selected = True
            break
        if Players ==3: #This is where the trained AI would go but Mine does not work
            print("\nYou have selected to play against a trianed AI (Not Working)")
            print("\nSorry this option is not available Currently\n")
            Been_Selected = False
            while Players ==3:
                Players = eval(input("\nInvalid Input \nOptions: \nPlay against a friend (1) \nPlay against an untrained computer (2) \nPlay against a trained AI (3) \nWhich Option do you take (1-3)?:"))
            continue
        else:#Handles if invalid input is given
            Players = eval(input("\nInvalid Input \nOptions: \nPlay against a friend (1) \nPlay against an untrained computer (2) \nPlay against a trained AI (3) \nWhich Option do you take (1-3)?:"))
def Player_Turn(Amount_of_Nuts, Turn_Number, Win = False):
    """Function that executes all that needs to be done during a players turn"""
    if Win ==False:#As long as the last nut has not been taken
        if ((Turn_Number%2) == 0):
            Player = "Two"
        else:
            Player = "One"
        #print("\nTurn #: %d" %(Turn_Number)) #Lets you Know what Turn number the Game is on
        print("\nPlayer %s Turn:" %(Player))
        Player_Turn = (eval(input("How many Nuts do you take (1-3)?:")))
        if ((Player_Turn >=1) and (Player_Turn <= 3)):
           Amount_of_Nuts = (Amount_of_Nuts - Player_Turn)
        else:#If a value outside of the range is given (1-3)
            while (Player_Turn < 1) or (Player_Turn > 3):
                Player_Turn = (eval(input("Invalid selection, try again \nHow many Nuts do you take (1-3)?:")))

         #This is everything that happens after Player one's turn once a valid input has been provided during the turn
        if Amount_of_Nuts !=0:
            print("Amount of nuts remaining %d" %(Amount_of_Nuts))
        
    return Amount_of_Nuts
def Win_Condition(Amount_of_Nuts,name = None, Turn_Number=0, Players = 0, Hats = 0 ):
    """Handles checking if the game has been won, and if it has prints which Player won, and then asks if you would like to play again and handles the selection made: Takes the current amount of nuts, class Name, Turn number, Players, and Hats list as arguments"""
    if (Amount_of_Nuts <= 0): #If the last nut has been taken
        Win = True
        if Players == 1: #If you are playing a Human vs Human game; this is the default state
            if not (Turn_Number % 2 == 0):
                print("\nPlayer One Wins")
            if (Turn_Number % 2 == 0):
                print("\nPlayer Two Wins")                           
        if (Players == 2 or Players ==3): #If you are playing against an AI, the game will print the right message corresponding to whoever won
            if not (Turn_Number % 2 == 0):
                print("\nAI Wins")
                name.incrementing_Moves(Hats_class.Moves_Made, Hats) #Adds +2 to any value that was decremented previously
            if (Turn_Number % 2 == 0):
                print("\nPlayer One Wins")                                                
            repeat = eval(input("\nWould You Like to play again? \n1 for Yes \n2 for No: ")) #After the game has been won it will ask if you would like to play again
            if repeat == 1: # if someone wants to play again
                Main()
            if repeat == 2:            
                print('\nThanks For playing')
                pass
            else: #Handles if you type in a variable outside of range for repeat(1-2)
                while not ((repeat == 1) or (repeat == 2)):
                    repeat = eval(input("\nInvalid Option Selected Please Choose one of the Below options: \nWould You Like to play again? \n1 for Yes 2, for No \nI choose:"))
                    if repeat == 1:
                        Main()
                    if repeat == 2:            
                        print('\nThanks For playing \n')
                        pass
        elif Players == 5:
            pass
        return Win

    else: #If the last nut has not yet been taken
        Win = False
    return Win
def Main():
    """The main function that will get called to play the game"""
    print("\nWelcome to the game of nuts!\n")
    Player_Number(How_Many_Nuts())
    pass    

#Section 2: In this section I will be defining all the Functions for Player vs Player specific games   
def Player_vs_Player(Amount_of_Nuts,Players):
    """This is the function that defines what should happen if the Player vs Player mode is selected: Takes Amount of nuts and players as arguments"""
    Turn_Number = 1 #is used to Let you Know what Turn number the Game is on for each Players turn + is used by Win_Condition to determine who won
    Win = Win_Condition(Amount_of_Nuts,Turn_Number, 1)#Initially sets up the Win Variable
    while Win == False:
            #Player Ones Turn
            Win = Win_Condition(Amount_of_Nuts,Turn_Number, 1)
            Amount_of_Nuts = Player_Turn(Amount_of_Nuts,Turn_Number,Win)
            Turn_Number += 1
            #Player two's Turn
            Win = Win_Condition(Amount_of_Nuts,Turn_Number, 1) #Updates Win Variable before Player One's Turn
            Amount_of_Nuts = Player_Turn(Amount_of_Nuts,Turn_Number,Win)
            Turn_Number += 1         

#Section 3: In this section I will be defining all the Functions for playing against and training the AI's
class Hats_class:
    """Class for handling Hats for the AI's"""
    Moves_Made = []
    def Tracking_Moves(name, Amount_of_Nuts,move, Moves_Made = None ):
        """This is the function that will track all the Moves made by the AI: Takes the class name, Amount of nuts, move chosen by the probability selection, and a None Type to check if a List already exists"""
        if Moves_Made == None:
            Moves_Made = []
        Moves_Made += [[(Amount_of_Nuts -1), move]]
        return(Moves_Made)
    def Init_Hats(name,Amount_of_Nuts):
        """Will create a list of lists (Hats) with the same amount of hats as nuts; to be used later to train the AI and to be used by the Probability_Selection"""
        Hats = []
        for i in range(Amount_of_Nuts):
            Hats += [[1,1,1]]
        return Hats
    def incrementing_Moves(Moves_Made, Hats):
        """Function that takes the list of Moves made by the AI and If it won Will increment the Values by 2: Takes The Moves Made and Hats as Arguments"""
        for i in range(len(Moves_Made)):
            [j,k] = Moves_Made[i]
            Hats[j][k] += 2            
def Probability_Selection(Current_Nuts_Hat,Hats,Amount_of_Nuts,name):
    """Function for selecting which value to go with based on the probability distribution"""    
    Total_Hat = (Current_Nuts_Hat[0] + Current_Nuts_Hat[1] + Current_Nuts_Hat[2])#Current_Nuts_Hat is the Hats Value of the current Nut; by default this is [1,1,1]
    r_int = random.randint(1, Total_Hat)
    Picked_Value = [1,2,3]
    if (r_int <= Current_Nuts_Hat[0]):
        move = 0
    elif (r_int <= Current_Nuts_Hat[0] + Current_Nuts_Hat[1]):
        move = 1
    else:
        move = 2
    Decrement_Hats(Current_Nuts_Hat, move,Amount_of_Nuts, name,Hats,) #after selecting a Value it is sent to Decrement_hats to decrement the value until the game is over 
    return Picked_Value[move]#Returns the value that has been selected by the AI                
def Decrement_Hats(Current_Nuts_Hat, move, Amount_of_nuts,name, Hats = 0, Win = False):
    """Function that decrements the value selected of the Hat until the game has been won or lost: Takes the Current Nuts hat, the Move selected py the probability selection, The Current amount of Nuts, the class name, Hats and if the game has been won or not as arguments"""
    if Win ==False:
        if Current_Nuts_Hat[move] == None:
            pass
        if Current_Nuts_Hat[move] > 0: # as long as the Hat value for the number selected is not alreafy 0
            Current_Nuts_Hat[move] = ((Current_Nuts_Hat[move]) - 1) #Decrement the Value selected by 1
        else:
            return Hats
    Hats_class.Moves_Made += Hats_class.Tracking_Moves(None, Amount_of_nuts,move) # send the decrement made to be tracked by Tracking_Moves

        
    return Hats
def AI_Turn(Hats, Amount_of_Nuts, Win, Turn_Number,name, Players = 5, Seen = 1):
    """Function that defines what should happen during an AI's Move: Takes Hats, the amount of nuts currently, If the game has been won or not yet, the Turn number, Class name, Player amount, and whether or not the Turn should  be seen as arguments"""
    Win = Win_Condition(Amount_of_Nuts,Turn_Number, Players)
    if Win == False: #Player one will be invalidated because of the while loop but in between the turns, the win variable dosen't get checked unless this if statement is present
        if Seen == 0:
            AI_Move = Probability_Selection(Hats[Amount_of_Nuts-1],Hats,Amount_of_Nuts,name) # picking the value that the AI will take from the table (Nuts between 1 and 3)
            Amount_of_Nuts = Amount_of_Nuts - AI_Move # subtracting the AI's selection from the current amount of nuts
        if Seen == 1:
            AI_Move = Probability_Selection(Hats[Amount_of_Nuts-1],Hats,Amount_of_Nuts,name)# picking the value that the AI will take from the table (Nuts between 1 and 3)
            print("\nAI's Turn; How many Nuts do you take (1-3)?: %d" %(AI_Move))
            Amount_of_Nuts = Amount_of_Nuts - AI_Move# subtracting the AI's selection from the current amount of nuts
    return Amount_of_Nuts
def Untrrained_AI(Amount_of_Nuts):
    """Function for playing against an untrained AI: Takes amount of nuts as arguments"""
    Turn_Number = 1 #is used to Let you Know what Turn number the Game is on for each Players turn + is used by Win_Condition to determine who won
    Players = 2
    Untrained_AI_Hats = Hats_class #Creating an Instance of Hats so they can be used elsewhere
    Hats = Untrained_AI_Hats.Init_Hats(None,Amount_of_Nuts) #Setting up the initial Hats for Untrained AI/Name
    Win = Win_Condition(Amount_of_Nuts,Untrained_AI_Hats,Turn_Number, Players, Hats)#Initially sets up the Win Variable
    while Win == False:
       #Player Ones Turn
        Amount_of_Nuts = Player_Turn(Amount_of_Nuts,Turn_Number,Win)
        Win = Win_Condition(Amount_of_Nuts,Untrained_AI_Hats, Turn_Number, Players, Hats)
        
        if Win == False:
            Turn_Number += 1        
        #AI's Turn
        Amount_of_Nuts = AI_Turn(Hats, Amount_of_Nuts, Win, Turn_Number,Untrained_AI_Hats, Players)
        Win = Win_Condition(Amount_of_Nuts,Untrained_AI_Hats,Turn_Number, Players, Hats)
       
        if Win == False:
            if Amount_of_Nuts <= 0:
                Win = True
                break
            else:
                Turn_Number += 1
                print("Amount of nuts remaining %d" %(Amount_of_Nuts))  

Main()

    
########################Section 4: Trained AI (Not Complete)#############################
def Trained_AI(Amount_of_Nuts, Trained_AI_Hats):
    """Function for playing against a Trained AI"""
    print("option Out of Order")
    #Players = 3
    #Turn_Number = 1 #is used to Let you Know what Turn number the Game is on for each Players turn + is used by Win_Condition to determine who won
    #Win = Win_Condition(Amount_of_Nuts,name,Turn_Number, Players)#Initially sets up the Win Variable
    #if Win ==False:#As long as the last nut has not been taken       
    #    Win = Win_Condition(Amount_of_Nuts,name,Turn_Number, Players) #Updates Win Variable before Player One's Turn
    #    while Win == False:
    #        #Player 1
    #        Win = Win_Condition(Amount_of_Nuts,None,Turn_Number, Players)
    #        Amount_of_Nuts = Player_Turn(Amount_of_Nuts,Turn_Number,Win)
    #        Turn_Number += 1           
    #        #AI's Turn
    #        Amount_of_Nuts = AI_Turn(Hats, Amount_of_Nuts, Win, Turn_Number,Trained_AI_Hats, Players)
    #        Win = Win_Condition(Amount_of_Nuts,Trained_AI_Hats,Turn_Number, Players, Hats)
    #        Turn_Number += 1
    #        if Win == False:
    #            if Amount_of_Nuts >= 0:
    #                print("Amount of nuts remaining %d" %(Amount_of_Nuts))
    #            if Amount_of_Nuts <= 0:
    #                Win = Win_Condition(Amount_of_Nuts,name,Turn_Number, Players)

def Train_AI(Old_number_of_Nuts):
    """This will be the function for training the trained AI"""
    print('Currently Out of Order')
    #Like_to_Continue = eval(input("Currently out of order, would you like to try it anyway?(1 for yes, 2 for No): "))
    #if (Like_to_Continue == 1):
    #    print("Training...\n")
    #    Amount_of_Nuts = 100
    #    Trained_AI_Hats = Hats_class #Creating an Instance of Hats so they can be used elsewhere
    #    name = Trained_AI_Hats #Assigning the instance a more friendly name
    #    Hats = Trained_AI_Hats.Init_Hats(None,Amount_of_Nuts) #Setting up the initial Hats for Trained AI/Name
    #
    #    Training_AI_Hats = Hats_class #Creating an Instance of Hats so they can be used elsewhere
    #    name = Training_AI_Hats #Assigning the instance a more friendly name
    #    Hats1 = Training_AI_Hats.Init_Hats(None,Amount_of_Nuts) #Setting up the initial Hats for Training AI/Name
    #    Players = 5
    #    Turn_Number = 1
    #    Win = Win_Condition(Amount_of_Nuts,Turn_Number, Players)#Initially sets up the Win Variable
    #    for i in range(10):
    #        if Win == True:
    #            Decrement_Hats(None, None,Amount_of_Nuts, Hats, True)
    #
    #        Turn_Number = 1
    #        Amount_of_Nuts = 100
    #        Win = Win_Condition(Amount_of_Nuts,Turn_Number, Players)#Initially sets up the Win Variable
    #        while Win == False:
    #            #AI ones
    #            Amount_of_Nuts = AI_Turn(Hats, Amount_of_Nuts, Win, Turn_Number,Trained_AI_Hats, Players,0)
    #            Win = Win_Condition(Amount_of_Nuts,Trained_AI_Hats,Turn_Number, Players, Hats)
    #            if Win == False:
    #                if Amount_of_Nuts <= 0:
    #                    Win = Win_Condition(Amount_of_Nuts,name,Turn_Number, Players)
    #            Turn_Number += 1        
    #            #AI's Turn
    #            Amount_of_Nuts = AI_Turn(Hats, Amount_of_Nuts, Win, Turn_Number,Training_AI_Hats, Players,0)
    #            Win = Win_Condition(Amount_of_Nuts,Training_AI_Hats,Turn_Number, Players, Hats)
    #            if Win == False:
    #                if Amount_of_Nuts <= 0:
    #                    Win = Win_Condition(Amount_of_Nuts,Training_AI_Hats,Turn_Number, Players)
    #            Turn_Number += 1
    #        Hats = Hats
    #    print(Hats)
    #    print("\nAmount of nuts remaining %d" %(Old_number_of_Nuts))
    #    Trained_AI(Old_number_of_Nuts, Training_AI_Hats)
    #elif Like_to_Continue == 2:
    #    print("Good Choice")
    pass
            
