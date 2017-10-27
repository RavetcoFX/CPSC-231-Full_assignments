def create_window():
    """Function that will create the window the game will be played in"""
    pass

def Set_Up_Initial_Variables():
    """The function that asks all the initial questions to get the game started"""
    Valid_input = False
    while Valid_input == False:
        Amount_of_Nuts = (eval(input("How many nuts are there on the table initially (10-100)?")))
        if (10 <= Amount_of_Nuts) and (Amount_of_Nuts <= 100):
           print((('%d Nuts Selected, The game will begin counting down from: %d nuts' % (Amount_of_Nuts,Amount_of_Nuts))))
           Valid_input = True
        while Valid_input == False:
           Amount_of_Nuts = eval(input("Invalid amount chosen please select a value for the amount of nuts on the table initially (10-100):"))
           if (10 <= Amount_of_Nuts) and (Amount_of_Nuts <= 100):
               print((('%d Nuts Selected, The game will begin counting down from: %d nuts' % (Amount_of_Nuts,Amount_of_Nuts))))
               Valid_input = True
           else:
               Valid_input = False
    return Amount_of_Nuts
     
def endgame_repeat():
    repeat = eval(input("would You Like to play again? \n1 for Yes \n2 for no"))
    if repeat == 1:
        main()
    else:
        pass
        



def How_Many_Players(Amount_of_Nuts):
    """function that will give you an input option to choose if you want to play with one or two players"""
    Players = eval(input("Options: \nPlay against a friend (1) \nPlay against an untrained computer (2) \nPlay against a trained AI (3) \nWhich Option do you take (1-3)?:"))
    selection = 0
    while selection == 0:
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
           
    endgame_repeat()

def Player_vs_Player(Amount_of_Nuts,Players):
    if Players == 1:
        while Amount_of_Nuts != 0:
            Player_one_Turn = (eval(input("Player one; How many Nuts do you take (1-3)?:")))
            Player_two_Turn = (eval(input("Player two; How many Nuts do you take (1-3)?:")))
            
            if (Player_one_Turn >=1) and (Player_one_Turn <= 3):
               Amount_of_Nuts - Player_one_Turn
            if not ((Player_one_Turn >=1) and (Player_one_Turn <= 3)):
                while (Player_one_Turn < 1) or (Player_one_Turn > 3):
                    Player_one_Turn = (eval(input("Invalid selection, try again \nPlayer one; How many Nuts do you take (1-3)?:")))

            Amount_of_Nuts - Player_two_Turn
        pass 
       




def Main():
    """The main function that will get called to play the game"""
    print("Welcome to the game of nuts!")
    
    How_Many_Players(Set_Up_Initial_Variables())
    pass
 

def initHats(amountofnuts):
    """will create a list with the same amount of hats as nuts"""
    hats = []
    for i in range(amountofnuts):
        hats += [[1,1,1]]
    print(hats)

 


Main()