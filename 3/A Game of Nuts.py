def create_window():
    """Function that will create the window the game will be played in"""
    pass
def Set_Up_Initial_Variables():
    Amount_of_Nuts = (eval(input("How many nuts are there on the table initially (10-100)?")))
    print((('%d Nuts Selected, The game will begin counting down from: %d nuts' % (Amount_of_Nuts,Amount_of_Nuts))))


def How_Many_Players():
    """function that will give you an input option to choose if you want to play with one or two players"""
    Players = eval(input("Options: \nPlay against a friend (1) \nPlay against an untrained computer (2) \nPlay against a trained AI (3) \nWhich Option do you take (1-3)?:"))
    slection = 0
    while selection == 0:
        if Players == 1:
            print("You have selected a two player game")
            selection =1
            break
        if Players ==2:
            print("You have selected to play against an untrianed AI")
            selection =1
            break
        if Players == 3:
            print("You have selected to play against a trianed AI")
            selection =1
            break
        else:
            print("please select a valid option")
            selection = 0 
            break
    pass

def Main():
    """The main function that will get called to play the game"""
    print("Welcome to the game of nuts!")
    Set_Up_Initial_Variables()
    How_Many_Players()
    pass

Main()