#Assignment 3 - A game of nuts - Kieran Wood

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
    Players = eval(input("Options: \nPlay against a friend (1) \nPlay against an untrained computer (2) \nPlay against a trained AI (3) \nWhich Option do you take (1-3)?:"))
    selection = 0
    Win = endgame_repeat(Amount_of_Nuts) # Because this is the outermost function being called in the Main function it needs to know if it should terminate
    while ((selection == 0) and (Win == False)):
        if Players == 1:
            print("You have selected a two player game")
            selection =1
            Player_vs_Player(Amount_of_Nuts,Players)
            break
        if Players ==2:
            print("You have selected to play against an untrianed AI")
            selection =1
            break
        if Players == 3:
            print("You have selected to play against a trianed AI, Good Luck Have Fun")
            selection =1
            break
        else:
            print("please select a valid option")
            selection = 0 
    pass
           
    

def Player_vs_Player(Amount_of_Nuts,Players):
    Win = endgame_repeat(Amount_of_Nuts)
    if ((Players == 1) and (Win ==False)):
        Win = endgame_repeat(Amount_of_Nuts)
        while Win == False:
            Player_one_Turn = (eval(input("Player one; How many Nuts do you take (1-3)?:")))
            if ((Player_one_Turn >=1) and (Player_one_Turn <= 3)):
               Amount_of_Nuts = Amount_of_Nuts - Player_one_Turn
            if not ((Player_one_Turn >=1) and (Player_one_Turn <= 3)):
                while (Player_one_Turn < 1) or (Player_one_Turn > 3):
                    Player_one_Turn = (eval(input("Invalid selection, try again \nPlayer one; How many Nuts do you take (1-3)?:")))

            print("Amount of nuts remaining %d" %(Amount_of_Nuts))
            print(Win)

            Win = endgame_repeat(Amount_of_Nuts)
            if Win == False: #Player one will be invalidated because of the while loop but in between the turns, the win variable dosen't get checked
                Player_two_Turn = (eval(input("Player two; How many Nuts do you take (1-3)?:")))
                if ((Player_two_Turn >=1) and (Player_two_Turn <= 3)):
                   Amount_of_Nuts = Amount_of_Nuts - Player_two_Turn
                if not ((Player_two_Turn >=1) and (Player_two_Turn <= 3)):
                    while (Player_two_Turn < 1) or (Player_two_Turn > 3):
                        Player_two_Turn = (eval(input("Invalid selection, try again \nPlayer one; How many Nuts do you take (1-3)?:")))
                print(Win)


                print("Amount of nuts remaining %d" %(Amount_of_Nuts))
            
    else:
        pass 
       
def initHats(amountofnuts):
    """will create a list with the same amount of hats as nuts"""
    hats = []
    for i in range(amountofnuts):
        hats += [[1,1,1]]
    print(hats)


def endgame_repeat(Amount_of_Nuts):
    if (Amount_of_Nuts <= 0):
        Win = True
        repeat = eval(input("Would You Like to play again? \n1 for Yes 2, for No \nI choose:"))
        if repeat == 1:
            Main()
        if repeat == 2:
            print('Thanks For playing')
            return Win

        else:
            repeat = eval(input("Invalid Option Selected Please Choose one of the Below options: \nWould You Like to play again? \n1 for Yes 2, for No \nI choose:"))
    else:
        Win = False
    return Win
       

def Main():
    """The main function that will get called to play the game"""
    print("Welcome to the game of nuts!")
    
    How_Many_Players(Set_Up_Initial_Variables())
    pass
 


 


Main()