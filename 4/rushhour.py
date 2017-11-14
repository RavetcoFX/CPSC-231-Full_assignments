#assignment 4 - Kieran Wood

class Blocker:
    """This will be the class that defines the blockers/None-Goal Car"""
    carnumber = 1
    def __init__(self):
        self.carnumber = carnumber
        carnumber += 1
    def __del__(self):
        carnumber -= 1 
        pass
        
    pass

class Goal_Car:
    """This is the class that will be the player/Goal Car"""
    carnumber = 1
    def __init__(self):
        self.carnumber = Goal_Car.carnumber
        Goal_Car.carnumber += 1
        self.display = [[self.carnumber]]

class Game:
    def Init_Grid(Goal_Car, Blockers):
        """Creates the initial grid that the user will play from; needs to call place cars"""
        verticle = 6
        Horizontal = 6
        for i in range(verticle):#creates the verticle spacing using the horizontal elements created within the for loop
            Container_List = []
            Base_Value = [[1]]
            Container_List += (Base_Value*Horizontal) #Creates the horizontal elements of the grid
            print(Container_List)
    def Turn(Car, Row, Collum):
        """The function that will define taking the turn"""
        #move car to the row location
        #move car to collum location
        pass
    def Place_cars(Car, Row , Collum):
        """Will need to be able to place the cars in their initial locations reading from the file provided"""
        pass


print(Goal_Car.carnumber)
Kyle = Goal_Car()
jamie = Goal_Car()

print(Kyle.carnumber, jamie.carnumber)

Game.Init_Grid(None, None)