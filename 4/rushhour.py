#assignment 4 - Kieran Wood

class Cars:
    """This is the class that will be the player/Goal Car"""
    carnumber = 1
    x = 0
    y = 0
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

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x
    
    def set_y(self, new_y):
        self.y = new_y

class Game:
    car_number = 6
    car_dict = {}
    for i in range(car_number):
        car_dict['car_%i' %(i)] = Cars()

    def Update_Grid(car_num):
        """Creates the initial grid that the user will play from; needs to call place cars"""
        vertical = 6
        horizontal = 6

        Container_List = []
        current_car = Game.car_dict['car_%i' %(car_num)]
        for i in range(0,vertical):#creates the verticle spacing using the horizontal elements created within the for loop
            Car_row = current_car.get_x()
            Car_collum = current_car.get_y()
            Car_orientation = ('h')
            Empty_Value = [0] #The Value for empty space
            Container_List.append(Empty_Value*horizontal) #Creates the horizontal elements of the grid
            #Container_List.append(str(i))
        if Car_orientation == ('h'):
            Container_List[Car_row-1][Car_collum-1] = 1
            Container_List[Car_row-1][Car_collum-2] = 1
        print (Container_List)
        print("\n Grid version\n")
        return Container_List

    def Turn():
        """The function that will define taking the turn"""
        [number, collumn_y, row_x] = eval(input("Please select a Car Number, The collum you would like to move the car to, and the row you would like to move the car to:"))
        current_car = Game.car_dict['car_%i' %(number)]
        current_car.set_y(collumn_y)
        current_car.set_x(row_x)
        print("Car #%i new positon is: X=%i Y=%i" %(number, current_car.get_x(), current_car.get_y()))
        Game.Update_Grid(number)


print("Initial Count\n")
print(Cars.carnumber)
print("Final Count\n")
print(Cars.carnumber)



Game.Update_Grid(0)
Game.Turn()


import sys

#if __name__ == '__main__':
#    if len (sys.argv) != 2:
#        sys.stderr.write()
#        sys.exit()
