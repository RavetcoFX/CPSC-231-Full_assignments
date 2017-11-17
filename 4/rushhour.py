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

    def current_row(self):
        pass
    def current_collum(self):
        pass

    

class Game:
    def Init_Grid(Goal_Car, Blockers):
        """Creates the initial grid that the user will play from; needs to call place cars"""
        verticle = 6
        Horizontal = 6
        for i in range(verticle):#creates the verticle spacing using the horizontal elements created within the for loop
            Container_List = []
            Empty_Value = ' █ ' #The Value for empty space
            Container_List += (Empty_Value*Horizontal) #Creates the horizontal elements of the grid
            Container_List += '\n'
            i=0
            result = ''
            for i in range (len(Container_List)):
                result += (Container_List[i])
                
            print (result)
    def Turn(Car, Row, Collum):
        """The function that will define taking the turn"""
        #move car to the row location
        #move car to collum location
        pass
    def Place_cars(Car, Row , Collum):
        """Will need to be able to place the cars in their initial locations reading from the file provided"""
        pass


#print(Goal_Car.carnumber)
#Kyle = Goal_Car()
#jamie = Goal_Car()

#print(Kyle.carnumber, jamie.carnumber)

Game.Init_Grid(None, None)

import sys

#if __name__ == '__main__':
#    if len (sys.argv) != 2:
#        sys.stderr.write()
#        sys.exit()