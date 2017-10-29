#Assignment 3 - A game of nuts - Kieran Wood


#Setting up the functions that will be used for each case of the game; Player vs Player, Player vs Untrained AI, Player vs Trained AI
def Set_Up_Initial_Variables():
    """The function that asks for how many nuts you would like to initially start with"""
    Valid_input = False #Variable to decide whther the input given is within range (1-100)
    while Valid_input == False:
        Amount_of_Nuts = (eval(input("How many nuts are there on the table initially (10-100)?")))
        if (10 <= Amount_of_Nuts) and (Amount_of_Nuts <= 100): #If the amount of nuts is in range
           print((('%d Nuts Selected, The game will begin counting down from: %d nuts' % (Amount_of_Nuts,Amount_of_Nuts))))
           Valid_input = True
        while Valid_input == False: #If the amount of nuts is not in range 
           Amount_of_Nuts = eval(input("Invalid amount chosen please select a value for the amount of nuts on the table initially (10-100):"))
           if (10 <= Amount_of_Nuts) and (Amount_of_Nuts <= 100): #if the input value after the first time it is wrong is correct
               print((('%d Nuts Selected, The game will begin counting down from: %d nuts' % (Amount_of_Nuts,Amount_of_Nuts))))
               Valid_input = True
           else: #Should handle all other fringe cases
               Valid_input = False
    return Amount_of_Nuts     

def How_Many_Players(Amount_of_Nuts):
    """function that will give you an input option to choose if you want to play with one or two players"""
    Players = eval(input("\nOptions: \nPlay against a friend (1) \nPlay against an untrained computer (2) \nPlay against a trained AI (3) \nWhich Option do you take (1-3)?:"))
    selection = 0
    Turn_Number = 0
    Win = endgame_repeat(Amount_of_Nuts) # Because this is the outermost function being called in the Main function it needs to know if it should terminate
    while ((selection == 0) and (Win == False)):
        if Players == 1:
            print("\nYou have selected a two player game")
            selection =1
            Player_vs_Player(Amount_of_Nuts,Players)
            break
        if Players ==2:
            print("\nYou have selected to play against an untrianed AI")
            Untrrained_AI()
            selection =1
            break
        if Players == 3:
            print("\nYou have selected to play against a trianed AI, Good Luck Have Fun")
            Trained_AI()
            selection =1
            break
        else:
            while ((selection == 0) and (Win == False)):
                print("\nplease select a valid option:")
                Players = eval(input("\nPlay against a friend (1) \nPlay against an untrained computer (2) \nPlay against a trained AI (3) \nWhich Option do you take (1-3)?:"))
                if Players == 1:
                    print("\nYou have selected a two player game")
                    selection =1
                    Player_vs_Player(Amount_of_Nuts,Players)
                    break
                if Players ==2:
                    print("\nYou have selected to play against an untrianed AI")
                    Untrrained_AI()
                    selection =1
                    break
                if Players == 3:
                    print("\nYou have selected to play against a trianed AI, Good Luck Have Fun")
                    Trained_AI()
                    selection =1
                    break
                else:
                    selection = 0 
    pass

def endgame_repeat(Amount_of_Nuts,Turn_Number=0):
    """Handles checking if the game has been won, and if it has prints which player won, and then asks if you would like to play again and handles the selection made"""
    if (Amount_of_Nuts <= 0): #If the last nut has been taken
        Win = True
        if not (Turn_Number % 2 == 0):
                print("Player One Wins")
        if (Turn_Number % 2 == 0):
            print("\nPlayer Two Wins")
        
        repeat = eval(input("\nWould You Like to play again? \n1 for Yes 2, for No \nI choose:"))
        if repeat == 1:
            print('')
            Main()
        if repeat == 2:            
            print('\nThanks For playing')
            return Win

        else: #Handles id you type in a variable outside of range (1-2)
            while not ((repeat == 1) or (repeat == 2)):
                repeat = eval(input("\nInvalid Option Selected Please Choose one of the Below options: \nWould You Like to play again? \n1 for Yes 2, for No \nI choose:"))
                if repeat == 1:
                    Main()
                if repeat == 2:            
                    print('\nThanks For playing \n')
                    return Win

    else: #If the last nut has not yet been taken
        Win = False
    return Win

def Main():
    """The main function that will get called to play the game"""
    print("Welcome to the game of nuts!")
    
    How_Many_Players(Set_Up_Initial_Variables())
    pass    

#Functions for Player vs Player
    

def Player_vs_Player(Amount_of_Nuts,Players):
    """This is the function that defines what should happen if the Player vs Player mode is selected"""
    Turn_Number = 1 #is used to Let you Know what Turn number the Game is on for each players turn + is used by endgame_repeat to determine who won
    Win = endgame_repeat(Amount_of_Nuts,Turn_Number)#Initially sets up the Win Variable

    if Win ==False:#As long as the last nut has not been taken       
        Win = endgame_repeat(Amount_of_Nuts,Turn_Number) #Updates Win Variable before Player One's Turn
        while Win == False:
            #Player One's Turn

            print("\nTurn #: %d" %(Turn_Number)) #Lets you Know what Turn number the Game is on
            Player_one_Turn = (eval(input("Player one; How many Nuts do you take (1-3)?:")))
            if ((Player_one_Turn >=1) and (Player_one_Turn <= 3)):
               Amount_of_Nuts = Amount_of_Nuts - Player_one_Turn
            if not ((Player_one_Turn >=1) and (Player_one_Turn <= 3)):#If a value outside of the range is given (1-3)
                while (Player_one_Turn < 1) or (Player_one_Turn > 3):
                    Player_one_Turn = (eval(input("Invalid selection, try again \nPlayer one; How many Nuts do you take (1-3)?:")))

             #This is everything that happens after player one's turn once a valid input has been provided during the turn
            Turn_Number += 1
            if Amount_of_Nuts !=0:
                print("Amount of nuts remaining %d" %(Amount_of_Nuts))
            
            #Player Two's Turn
            Win = endgame_repeat(Amount_of_Nuts,Turn_Number) #Updating the Win Status before Player Two's Turn
            if Win == False: #Player one will be invalidated because of the while loop but in between the turns, the win variable dosen't get checked unless this if statement is present
                print("\nTurn #: %d" %(Turn_Number))#Lets you Know what Turn number the Game is on
                Player_two_Turn = (eval(input("Player two; How many Nuts do you take (1-3)?:")))
                if ((Player_two_Turn >=1) and (Player_two_Turn <= 3)):
                   Amount_of_Nuts = Amount_of_Nuts - Player_two_Turn
                if not ((Player_two_Turn >=1) and (Player_two_Turn <= 3)):#If a value outside of the range is given (1-3)
                    while (Player_two_Turn < 1) or (Player_two_Turn > 3):
                        Player_two_Turn = (eval(input("Invalid selection, try again \nPlayer one; How many Nuts do you take (1-3)?:")))

                #This is everything that happens after player two's turn once a valid input has been provided during the turn
                Turn_Number += 1
                if Amount_of_Nuts != 0:
                    print("Amount of nuts remaining %d" %(Amount_of_Nuts))
                if Amount_of_Nuts == 0:
                    Win = endgame_repeat(Amount_of_Nuts,Turn_Number)

            
    else:
        pass 

#Functions for AI's
       
def initHats(Amount_of_Nuts):
    """will create a list with the same amount of hats as nuts"""
    hats = []
    for i in range(Amount_of_Nuts):
        hats += [[1,1,1]]
    print(hats)
    return hats

def Probability_Selection():
    """Function for selecting which value to go with based on the probability distribution"""
    pass

def Untrrained_AI():
    """Function for playing against an untrained AI"""
    print("Hue I suck")
    pass

def Trained_AI():
    """Function for playing against a Trained AI"""
    print("Hue I Win")
    pass


       


 


 


Main()