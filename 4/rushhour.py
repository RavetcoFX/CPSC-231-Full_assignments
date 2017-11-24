#assignment 4 - Kieran Wood

class Cars:
    """This is the class that will be the player/Goal Car"""
    carnumber = 1
    def __init__(self):
        self.carnumber = Cars.carnumber
        Cars.carnumber += 1
        self.display = [[self.carnumber]]
    def Starting_Pos(self, Position, Orientation):
        """Defines where the car will start from, gets called from the file reading function"""
        self.x = Position[0]
        self.y = Position[1]
        self.Orientation = Orientation
        return [self.x,self.y,self.Orientation]

    x = 0
    y = 0

    

class Game:

    Car_One = Cars()
    Car_Two = Cars()
    Car_Three = Cars()
    Car_Four = Cars()
    Car_Five = Cars()
    Car_Six = Cars()


    def Update_Grid(self):
        """Creates the initial grid that the user will play from; needs to call place cars"""
        verticle = 6
        Horizontal = 6
        count = 0
        Container_List = []
        for i in range(0,verticle):#creates the verticle spacing using the horizontal elements created within the for loop
            Car_row = 2
            Car_collum = 2
            Car_orientation = ('h')



            count += 1 
            Empty_Value = [0] #The Value for empty space
            Container_List.append(Empty_Value*Horizontal) #Creates the horizontal elements of the grid
            #Container_List.append(str(i))
        if Car_orientation == ('h'):
            Container_List[Car_row-1][Car_collum-1] = 1
            Container_List[Car_row-1][Car_collum-2] = 1
        print (Container_List)
        print("\n Grid version\n")
        return Container_List

    def Turn(Car):
        """The function that will define taking the turn"""
        [Car_Number, New_Collum, New_Row] = eval(input("Please select a Car Number, The collum you would like to move the car to, and the row you would like to move the car to: "))
        Car.self.x = New_Row
        print(Car.self.x)
        print (Car_Number)
        print (New_Collum)
        print (New_Row)
        #move car to the row location
        #move car to collum location
        pass
    def Place_cars(Car, Row , Collum):
        """Will need to be able to place the cars in their initial locations reading from the file provided"""

        pass


print("Initial Count\n")
print(Cars.carnumber)
print('Cars:\n')
print(Game.Car_One.carnumber)
print(Game.Car_Two.carnumber)
print(Game.Car_Three.carnumber)
print(Game.Car_Four.carnumber)
print(Game.Car_Five.carnumber)
print(Game.Car_Six.carnumber)
print("Final Count\n")
print(Cars.carnumber)
Game.Update_Grid(None)


import sys

#if __name__ == '__main__':
#    if len (sys.argv) != 2:
#        sys.stderr.write()
#        sys.exit()