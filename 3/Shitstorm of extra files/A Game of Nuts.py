#Assignment 3 - A game of nuts - Kieran Wood

#I have split the code up into sections to make it easier to jump between sections to mark;
#Section 1: All the general game functions that every case uses
#Section 2: All the Player vs Player specific functions
#Section 3: All the Player vs Untrained AI and Player vs Trained AI, aswell as the training functions

import random #The Library that will allow the random number generation needed in the Probability_Selection Function

#Section 1: Defining the functions that will be used for each case of the game; Player vs Player, Player vs Untrained AI, Player vs Trained AI  




def endgame_repeat(Amount_of_Nuts,Turn_Number=0, Players = 0):
    """Handles checking if the game has been won, and if it has prints which Player won, and then asks if you would like to play again and handles the selection made"""
    if (Amount_of_Nuts <= 0): #If the last nut has been taken
        Win = True
        if Players == 1: #If you are playing a Human vs Human game; this is the default state
            if not (Turn_Number % 2 == 0):
                print("\nPlayer One Wins")
            if (Turn_Number % 2 == 0):
                print("\nPlayer Two Wins")
        if Players == (2 or 3): # if you are playing against one of the AI's
            if not (Turn_Number % 2 == 0):
                print("\nPlayer One Wins")
            if (Turn_Number % 2 == 0):
                print("\nAi Wins")
        if (Players == 4):
            if not (Turn_Number % 2 == 0):
                print("\nAI One Wins")
            if (Turn_Number % 2 == 0):
                print("\nAi Two Wins")   
        if Players == 5:
            pass
                
        if Players != 5:        
            repeat = eval(input("\nWould You Like to play again? \n1 for Yes \n2 for No: "))
            if repeat == 1:
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
    print("\nWelcome to the game of nuts!")
    instructions = eval(input("\nWould you like to see the instructions? \n1 for Yes \n2 for No: "))
    if instructions == 1:
        print("\nThis is a game in which after selecting the initial amount of nuts for the game Players will take turns removing nuts. \nThe objective of the game is to force your opponent to take the last nut on the table.\n ")
    if instructions ==2:
        pass
    else:
        pass
    How_Many_Players(Set_Up_Initial_Variables())
    pass    



#Section 3: In this section I will be defining all the Functions for playing against and training the AI's
       
def initHats(Amount_of_Nuts):
    """Will create a list of lists (Hats) with the same amount of hats as nuts; to be used later to train the AI and to be used by the Probability_Selection"""
    Hats = []
    for i in range(Amount_of_Nuts):
        Hats += [[5,5,5]]
    return Hats

def Probability_Selection(Current_Nuts_Hat,Hats,Amount_of_Nuts):
    """Function for selecting which value to go with based on the probability distribution"""
    # Current_Nuts_Hat is the Hats Value of the current Nut; by default this is [1,1,1]
    Total_Hat = (Current_Nuts_Hat[0] + Current_Nuts_Hat[1] + Current_Nuts_Hat[2])
    print(Total_Hat)
    r_int = random.randint(1, Total_Hat)
    Picked_Value = [1,2,3]
    if (r_int <= Current_Nuts_Hat[0]):
        move = 0
    elif (r_int <= Current_Nuts_Hat[0] + Current_Nuts_Hat[1]):
        move = 1
    else:
        move = 2
    return [Picked_Value[move]
                
def Decrement_Hats(Current_Nuts_Hat, move, Amount_of_nuts, Hats = 0, Win = False):
    """Function that decrements the value selected of the Hat until the game has been won or lost"""
    Moves_Made = []
    Moves_Made += [[(Amount_of_nuts -1), move]]
    print(Moves_Made)
    if Win ==False:
        if Current_Nuts_Hat[move] > 0:
            Current_Nuts_Hat[move] = ((Current_Nuts_Hat[move]) - 1)
        else:
            return Hats
        
    for i in range(len(Moves_Made)):
        if Win == False:
            pass
        if Win == True:
            (j,k) = Moves_Made[i]
            Hats[j][k] += 2
            print('\nNew Hats')
            print(Hats)
        
    return Hats

def AI_Turn(Hats, Amount_of_Nuts, Win, Turn_Number,Players = 5, Seen = 1):
    Win = endgame_repeat(Amount_of_Nuts,Turn_Number, Players)
    if Win == True:
        Decrement_Hats(None, None,Amount_of_Nuts, Hats, True)
    if Win == False: #Player one will be invalidated because of the while loop but in between the turns, the win variable dosen't get checked unless this if statement is present
        if Seen == 0:
            AI_Move = Probability_Selection(Hats[Amount_of_Nuts-1],Hats,Amount_of_Nuts)
            Decrement_Hats(Hats[Amount_of_Nuts-1],AI_Move, )
            Amount_of_Nuts = Amount_of_Nuts - AI_Move
        if Seen == 1:
            AI_Move = Probability_Selection(Hats[Amount_of_Nuts-1],Hats,Amount_of_Nuts)
            print("\nAI's Turn; How many Nuts do you take (1-3)?: %d" %(AI_Move))
            Amount_of_Nuts = Amount_of_Nuts - AI_Move
    return Amount_of_Nuts

def Untrrained_AI(Hats, Amount_of_Nuts):
    """Function for playing against an untrained AI"""
    Turn_Number = 1 #is used to Let you Know what Turn number the Game is on for each Players turn + is used by endgame_repeat to determine who won
    Players = 2
    Win = endgame_repeat(Amount_of_Nuts,Turn_Number, Players)#Initially sets up the Win Variable
    while Win == False:
       #Player Ones Turn
        Win = endgame_repeat(Amount_of_Nuts,Turn_Number, 1)
        Amount_of_Nuts = Player_Turn(Amount_of_Nuts,Turn_Number,Win)
        Turn_Number += 1        
        #AI's Turn
        Amount_of_Nuts = AI_Turn(Hats, Amount_of_Nuts, Win, Turn_Number, Players)
        Turn_Number += 1
        if Win == False:
            if Amount_of_Nuts >= 0:
                print("Amount of nuts remaining %d" %(Amount_of_Nuts))
            if Amount_of_Nuts <= 0:
                Win = endgame_repeat(Amount_of_Nuts,Turn_Number, Players)   

def Trained_AI(Amount_of_Nuts):
    """Function for playing against a Trained AI"""
    Players = 3
    Hats = initHats(Amount_of_Nuts)
    Turn_Number = 1 #is used to Let you Know what Turn number the Game is on for each Players turn + is used by endgame_repeat to determine who won
    Win = endgame_repeat(Amount_of_Nuts,Turn_Number, Players)#Initially sets up the Win Variable
    if Win ==False:#As long as the last nut has not been taken       
        Win = endgame_repeat(Amount_of_Nuts,Turn_Number, Players) #Updates Win Variable before Player One's Turn
        while Win == False:
            #Player 1
            Win = endgame_repeat(Amount_of_Nuts,Turn_Number, 1)
            Amount_of_Nuts = Player_Turn(Amount_of_Nuts,Turn_Number,Win)
            Turn_Number += 1           
            #AI's Turn
            Amount_of_Nuts = AI_Turn(Hats, Amount_of_Nuts, Win, Turn_Number, Players)
            Turn_Number += 1
            if Win == False:
                if Amount_of_Nuts >= 0:
                    print("Amount of nuts remaining %d" %(Amount_of_Nuts))
                if Amount_of_Nuts <= 0:
                    Win = endgame_repeat(Amount_of_Nuts,Turn_Number, Players)

def Training_AI(Old_number_of_Nuts):
    """This will be the function for training the trained AI"""
    print("Training...\n")
    Amount_of_Nuts = 100
    Hats = initHats(Amount_of_Nuts)
    Players = 5
    Turn_Number = 1
    Win = endgame_repeat(Amount_of_Nuts,Turn_Number, Players)#Initially sets up the Win Variable
    for i in range(10):
        if Win == True:
            Decrement_Hats(None, None,Amount_of_Nuts, Hats, True)

        Turn_Number = 1
        Amount_of_Nuts = 100
        Win = endgame_repeat(Amount_of_Nuts,Turn_Number, Players)#Initially sets up the Win Variable
        while Win == False:
            #AI ones
            Win = endgame_repeat(Amount_of_Nuts,Turn_Number, Players)#Initially sets up the Win Variable
            Amount_of_Nuts = AI_Turn(Hats, Amount_of_Nuts, Win,Turn_Number,Players, 0)
            Turn_Number += 1        
            #AI's Turn
            Win = endgame_repeat(Amount_of_Nuts,Turn_Number, Players)#Initially sets up the Win Variable
            Amount_of_Nuts = AI_Turn(Hats, Amount_of_Nuts, Win,Turn_Number, Players, 0)
            Turn_Number += 1
        Hats = Hats
    print(Hats)
    print("\nAmount of nuts remaining %d" %(Old_number_of_Nuts))
    Trained_AI(Old_number_of_Nuts)
            
        
        
        


Main()